"""Section 18 - Tries & String Algorithms (reference solutions)."""
from typing import List


class Trie:
    """Prefix tree over lowercase words.

    t = Trie(); t.insert("apple"); t.search("apple") -> True; t.search("app") -> False; t.starts_with("app") -> True
    Target: O(len(word)) per operation.
    """

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True  # end-of-word marker

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return bool(node and "$" in node)

    def starts_with(self, prefix: str) -> bool:
        return self._walk(prefix) is not None

    def _walk(self, s):
        node = self.root
        for ch in s:
            if ch not in node:
                return None
            node = node[ch]
        return node


class WordDictionary:
    """Add words, then search where '.' matches ANY single letter.

    add_word("bad"); search("b.d") -> True; search("..") -> False
    Target: DFS through a trie.
    """

    def __init__(self):
        self.root = {}

    def add_word(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return "$" in node
            ch = word[i]
            if ch == ".":
                return any(dfs(i + 1, child) for key, child in node.items() if key != "$")
            return ch in node and dfs(i + 1, node[ch])

        return dfs(0, self.root)


def longest_common_prefix(strs: List[str]) -> str:
    """Longest prefix shared by all strings ("" if none or list empty).

    longest_common_prefix(["flower","flow","flight"]) -> "fl"
    Target: O(total characters).
    """
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
    return prefix


def str_str(haystack: str, needle: str) -> int:
    """Index of the first occurrence of needle in haystack, or -1. Empty needle -> 0.
    Don't use str.find / index / in. Implement KMP.

    str_str("mississippi", "issip") -> 4
    Target: O(n + m) with KMP's failure (LPS) table.
    """
    if not needle:
        return 0
    lps = [0] * len(needle)  # lps[i] = length of longest proper prefix of needle[:i+1] that is also a suffix
    k = 0
    for i in range(1, len(needle)):
        while k and needle[i] != needle[k]:
            k = lps[k - 1]
        if needle[i] == needle[k]:
            k += 1
        lps[i] = k
    k = 0
    for i, ch in enumerate(haystack):
        while k and ch != needle[k]:
            k = lps[k - 1]  # fall back WITHOUT re-reading haystack
        if ch == needle[k]:
            k += 1
        if k == len(needle):
            return i - k + 1
    return -1


def longest_palindrome(s: str) -> str:
    """Longest palindromic SUBSTRING (any one if tied).

    longest_palindrome("babad") -> "bab" or "aba"
    Target: O(n^2) expand-around-center (Manacher's algorithm is O(n)).
    """
    best = ""
    for center in range(len(s)):
        for l, r in ((center, center), (center, center + 1)):  # odd and even length
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > len(best):
                best = s[l + 1:r]
    return best
