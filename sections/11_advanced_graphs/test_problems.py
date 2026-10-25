import pytest
from helpers import load

m = load(__file__)


@pytest.mark.parametrize("n,pre,exp", [(2, [[1, 0]], True), (2, [[1, 0], [0, 1]], False), (1, [], True), (3, [[1, 0], [2, 1]], True), (3, [[0, 1], [1, 2], [2, 0]], False)])
def test_can_finish(n, pre, exp):
    assert m.can_finish(n, pre) is exp


@pytest.mark.parametrize("n,pre", [(2, [[1, 0]]), (4, [[1, 0], [2, 0], [3, 1], [3, 2]]), (1, []), (3, [[0, 1], [1, 2]])])
def test_find_order_valid(n, pre):
    order = m.find_order(n, pre)
    assert sorted(order) == list(range(n))
    pos = {c: i for i, c in enumerate(order)}
    assert all(pos[b] < pos[a] for a, b in pre)


def test_find_order_cycle():
    assert m.find_order(2, [[1, 0], [0, 1]]) == []


@pytest.mark.parametrize("n,edges,exp", [(5, [[0, 1], [1, 2], [3, 4]], 2), (5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1), (4, [], 4)])
def test_count_components(n, edges, exp):
    assert m.count_components(n, edges) == exp


@pytest.mark.parametrize("edges,exp", [([[1, 2], [1, 3], [2, 3]], [2, 3]), ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4])])
def test_find_redundant_connection(edges, exp):
    assert m.find_redundant_connection(edges) == exp


@pytest.mark.parametrize("times,n,k,exp", [([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2), ([[1, 2, 1]], 2, 1, 1), ([[1, 2, 1]], 2, 2, -1)])
def test_network_delay_time(times, n, k, exp):
    assert m.network_delay_time(times, n, k) == exp


@pytest.mark.parametrize("pts,exp", [([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20), ([[3, 12], [-2, 5], [-4, 1]], 18), ([[0, 0]], 0)])
def test_min_cost_connect_points(pts, exp):
    assert m.min_cost_connect_points(pts) == exp


@pytest.mark.parametrize("n,fl,s,d,k,exp", [
    (4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1, 700),
    (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200),
    (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0, 500),
    (3, [[0, 1, 100]], 0, 2, 1, -1),
])
def test_find_cheapest_price(n, fl, s, d, k, exp):
    assert m.find_cheapest_price(n, fl, s, d, k) == exp
