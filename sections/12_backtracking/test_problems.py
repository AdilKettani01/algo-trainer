import pytest
from helpers import load

m = load(__file__)


def norm(lists):
    return sorted(sorted(x) for x in lists)


def test_subsets():
    assert norm(m.subsets([1, 2, 3])) == norm([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
    assert norm(m.subsets([0])) == [[], [0]]


def test_subsets_with_dup():
    res = m.subsets_with_dup([2, 1, 2])
    assert norm(res) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    assert len(res) == 6


def test_permutations():
    res = m.permutations([1, 2, 3])
    assert len(res) == 6 and sorted(map(tuple, res)) == sorted(__import__("itertools").permutations([1, 2, 3]))
    assert m.permutations([1]) == [[1]]


@pytest.mark.parametrize("c,t,exp", [([2, 3, 6, 7], 7, [[2, 2, 3], [7]]), ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]), ([2], 1, [])])
def test_combination_sum(c, t, exp):
    assert norm(m.combination_sum(c, t)) == exp


@pytest.mark.parametrize("n,exp", [(1, ["()"]), (3, ["((()))", "(()())", "(())()", "()(())", "()()()"])])
def test_generate_parenthesis(n, exp):
    assert sorted(m.generate_parenthesis(n)) == exp


def test_generate_parenthesis_count():
    assert len(m.generate_parenthesis(5)) == 42


@pytest.mark.parametrize("word,exp", [("ABCCED", True), ("SEE", True), ("ABCB", False)])
def test_exist(word, exp):
    board = [list("ABCE"), list("SFCS"), list("ADEE")]
    assert m.exist(board, word) is exp


@pytest.mark.parametrize("n,exp", [(1, 1), (4, 2), (6, 4), (8, 92)])
def test_total_n_queens(n, exp):
    assert m.total_n_queens(n) == exp
