import pytest
from helpers import load

m = load(__file__)


def g(*rows):
    return [list(r) for r in rows]


@pytest.mark.parametrize("grid,exp", [
    (g("11110", "11010", "11000", "00000"), 1),
    (g("11000", "11000", "00100", "00011"), 3),
    ([], 0), (g("0"), 0), (g("1"), 1),
])
def test_num_islands(grid, exp):
    assert m.num_islands(grid) == exp


@pytest.mark.parametrize("grid,exp", [
    ([[0, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]], 3), ([[0, 0, 0]], 0), ([[1, 1], [1, 1]], 4),
])
def test_max_area_of_island(grid, exp):
    assert m.max_area_of_island(grid) == exp


@pytest.mark.parametrize("grid,exp", [
    ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4), ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1), ([[0, 2]], 0), ([[0]], 0),
])
def test_oranges_rotting(grid, exp):
    assert m.oranges_rotting(grid) == exp


@pytest.mark.parametrize("grid,exp", [
    ([[0, 1], [1, 0]], 2), ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4), ([[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1), ([[0]], 1),
])
def test_shortest_path_binary_matrix(grid, exp):
    assert m.shortest_path_binary_matrix(grid) == exp


@pytest.mark.parametrize("graph,exp", [
    ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False), ([[1, 3], [0, 2], [1, 3], [0, 2]], True), ([[], []], True),
])
def test_is_bipartite(graph, exp):
    assert m.is_bipartite(graph) is exp


@pytest.mark.parametrize("b,e,words,exp", [
    ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
    ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
    ("a", "c", ["a", "b", "c"], 2),
])
def test_ladder_length(b, e, words, exp):
    assert m.ladder_length(b, e, words) == exp
