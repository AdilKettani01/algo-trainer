'Section 18 - Tries & String Algorithms (your workspace).'


from typing import List


class Trie:
    """Prefix tree over lowercase words.

    t = Trie(); t.insert("apple"); t.search("apple") -> True; t.search("app") -> False; t.starts_with("app") -> True
    Target: O(len(word)) per operation.
    """

    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def starts_with(self, prefix: str) -> bool:
        pass

    def _walk(self, s):
        pass


class WordDictionary:
    """Add words, then search where '.' matches ANY single letter.

    add_word("bad"); search("b.d") -> True; search("..") -> False
    Target: DFS through a trie.
    """

    def __init__(self):
        pass

    def add_word(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass


def longest_common_prefix(strs: List[str]) -> str:
    """Longest prefix shared by all strings ("" if none or list empty).

    longest_common_prefix(["flower","flow","flight"]) -> "fl"
    Target: O(total characters).
    """
    pass


def str_str(haystack: str, needle: str) -> int:
    """Index of the first occurrence of needle in haystack, or -1. Empty needle -> 0.
    Don't use str.find / index / in. Implement KMP.

    str_str("mississippi", "issip") -> 4
    Target: O(n + m) with KMP's failure (LPS) table.
    """
    pass


def longest_palindrome(s: str) -> str:
    """Longest palindromic SUBSTRING (any one if tied).

    longest_palindrome("babad") -> "bab" or "aba"
    Target: O(n^2) expand-around-center (Manacher's algorithm is O(n)).
    """
    pass
