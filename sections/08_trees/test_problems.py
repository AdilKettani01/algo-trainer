import pytest
from helpers import load, build_tree, tree_to_list, find_node

m = load(__file__)


@pytest.mark.parametrize("t,exp", [([3, 9, 20, None, None, 15, 7], 3), ([], 0), ([1, None, 2], 2), ([1], 1)])
def test_max_depth(t, exp):
    assert m.max_depth(build_tree(t)) == exp


def test_invert_tree():
    assert tree_to_list(m.invert_tree(build_tree([4, 2, 7, 1, 3, 6, 9]))) == [4, 7, 2, 9, 6, 3, 1]
    assert tree_to_list(m.invert_tree(build_tree([]))) == []


@pytest.mark.parametrize("t,exp", [([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]), ([1], [[1]]), ([], [])])
def test_level_order(t, exp):
    assert m.level_order(build_tree(t)) == exp


@pytest.mark.parametrize("t,exp", [
    ([2, 1, 3], True), ([5, 1, 4, None, None, 3, 6], False), ([5, 4, 6, None, None, 3, 7], False), ([2, 2, 2], False), ([], True),
])
def test_is_valid_bst(t, exp):
    assert m.is_valid_bst(build_tree(t)) is exp


@pytest.mark.parametrize("p,q,exp", [(5, 1, 3), (5, 4, 5), (6, 4, 5), (7, 8, 3)])
def test_lca(p, q, exp):
    root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    assert m.lowest_common_ancestor(root, find_node(root, p), find_node(root, q)).val == exp


@pytest.mark.parametrize("t,exp", [([1, 2, 3, 4, 5], 3), ([1, 2], 1), ([1], 0), ([], 0)])
def test_diameter(t, exp):
    assert m.diameter_of_binary_tree(build_tree(t)) == exp


@pytest.mark.parametrize("t,k,exp", [([3, 1, 4, None, 2], 1, 1), ([5, 3, 6, 2, 4, None, None, 1], 3, 3), ([5, 3, 6, 2, 4, None, None, 1], 6, 6)])
def test_kth_smallest(t, k, exp):
    assert m.kth_smallest(build_tree(t), k) == exp


@pytest.mark.parametrize("t,exp", [([1, 2, 3], 6), ([-10, 9, 20, None, None, 15, 7], 42), ([-3], -3), ([2, -1], 2)])
def test_max_path_sum(t, exp):
    assert m.max_path_sum(build_tree(t)) == exp
