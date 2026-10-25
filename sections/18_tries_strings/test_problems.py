import pytest
from helpers import load

m = load(__file__)


def test_trie():
    t = m.Trie()
    t.insert("apple")
    assert t.search("apple") is True
    assert t.search("app") is False
    assert t.starts_with("app") is True
    assert t.starts_with("b") is False
    t.insert("app")
    assert t.search("app") is True


def test_word_dictionary():
    w = m.WordDictionary()
    for word in ("bad", "dad", "mad"):
        w.add_word(word)
    assert w.search("pad") is False
    assert w.search("bad") is True
    assert w.search(".ad") is True
    assert w.search("b..") is True
    assert w.search("...") is True
    assert w.search("....") is False
    assert w.search("b.x") is False


@pytest.mark.parametrize("strs,exp", [(["flower", "flow", "flight"], "fl"), (["dog", "racecar", "car"], ""), (["a"], "a"), ([], ""), (["abc", "abc"], "abc")])
def test_longest_common_prefix(strs, exp):
    assert m.longest_common_prefix(strs) == exp


@pytest.mark.parametrize("h,n,exp", [("sadbutsad", "sad", 0), ("leetcode", "leeto", -1), ("abc", "", 0), ("aaaaa", "bba", -1), ("mississippi", "issip", 4), ("aabaaabaaac", "aabaaac", 4)])
def test_str_str(h, n, exp):
    assert m.str_str(h, n) == exp


@pytest.mark.parametrize("s,ok", [("babad", {"bab", "aba"}), ("cbbd", {"bb"}), ("a", {"a"}), ("forgeeksskeegfor", {"geeksskeeg"})])
def test_longest_palindrome(s, ok):
    assert m.longest_palindrome(s) in ok
