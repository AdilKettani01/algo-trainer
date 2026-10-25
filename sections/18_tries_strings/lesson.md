# 18 - Tries & String Algorithms

## Trie (prefix tree)
Each node maps a character → child; a flag marks "a word ends here". Insert/search/prefix are **O(L)** (L = word length), independent of how many words are stored.
```python
node = root
for ch in word:
    node = node.setdefault(ch, {})   # dict-of-dicts trie
node["$"] = True                     # end of word
```
Use for autocomplete, prefix counts, word-search boards, wildcard search (`.` → try every child with DFS), longest common prefix.

## KMP (substring search in O(n + m))
Naive search is O(n·m) because it re-reads text after a mismatch. KMP precomputes `lps[i]` = length of the longest **proper prefix of `needle[:i+1]` that is also a suffix**. On mismatch, fall back `k = lps[k-1]` instead of restarting - the text pointer never moves backward.

## Other tools to recognise
| Tool | Use |
|---|---|
| Rolling hash (Rabin-Karp) | many-pattern / substring-equality checks, repeated substrings |
| Z-function / Z-algorithm | pattern matching, string periodicity |
| Manacher | longest palindromic substring in O(n) |
| Suffix array / automaton | advanced substring queries |
| Aho-Corasick | match many patterns in one pass |

## Longest palindromic substring
**Expand around centre**: for each index try an odd centre `(i, i)` and an even centre `(i, i+1)`, expand while ends match. O(n²), O(1) space - plenty for interviews. (DP table is O(n²) space; Manacher is O(n).)

## String problem checklist
- Frequency array of 26 counts vs `Counter` vs sorted key.
- Sliding window for substrings (section 03).
- Two pointers for palindromes.
- DP for subsequences / edit distance (section 14).
- Strings are **immutable** in Python → `"".join(list_of_parts)` instead of `+=` in a loop.

**Practice:** `Trie`, `WordDictionary`, `longest_common_prefix`, `str_str`, `longest_palindrome`.
