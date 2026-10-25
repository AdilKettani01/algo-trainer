import random
import pytest
from helpers import load

m = load(__file__)


def test_lru_cache():
    c = m.LRUCache(2)
    c.put(1, 1); c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)
    assert c.get(2) == -1
    c.put(4, 4)
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4
    c.put(3, 30)  # update existing
    assert c.get(3) == 30


def test_fenwick_matches_bruteforce():
    rng = random.Random(1)
    n = 40
    ft, arr = m.FenwickTree(n), [0] * n
    for _ in range(300):
        i, d = rng.randrange(n), rng.randint(-9, 9)
        ft.update(i, d)
        arr[i] += d
        q = rng.randrange(n)
        assert ft.prefix_sum(q) == sum(arr[:q + 1])


def test_segment_tree():
    st = m.SegmentTree([5, 2, 8, 1])
    assert st.query_min(0, 2) == 2
    assert st.query_min(2, 3) == 1
    st.update(3, 9)
    assert st.query_min(2, 3) == 8
    assert st.query_min(0, 3) == 2


def test_segment_tree_random():
    rng = random.Random(5)
    arr = [rng.randint(-100, 100) for _ in range(37)]
    st = m.SegmentTree(arr)
    for _ in range(300):
        if rng.random() < .4:
            i, v = rng.randrange(len(arr)), rng.randint(-100, 100)
            arr[i] = v
            st.update(i, v)
        l = rng.randrange(len(arr)); r = rng.randrange(l, len(arr))
        assert st.query_min(l, r) == min(arr[l:r + 1])


@pytest.mark.parametrize("nums,k,exp", [([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]), ([1], 1, [1]), ([9, 11], 2, [11]), ([4, 3, 2, 1], 2, [4, 3, 2])])
def test_sliding_window_maximum(nums, k, exp):
    assert m.sliding_window_maximum(nums, k) == exp
