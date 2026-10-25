"""Section 15 - Greedy Algorithms (reference solutions)."""
from math import inf
from typing import List


def max_sub_array(nums: List[int]) -> int:
    """Largest sum of a contiguous non-empty subarray (Kadane's algorithm).

    max_sub_array([-2,1,-3,4,-1,2,1,-5,4]) -> 6
    Target: O(n), O(1) space.
    """
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)  # extend the run, or start fresh here
        best = max(best, cur)
    return best


def can_jump(nums: List[int]) -> bool:
    """nums[i] = max jump length from i. Starting at index 0, can you reach the last index?

    can_jump([2,3,1,1,4]) -> True ; can_jump([3,2,1,0,4]) -> False
    Target: O(n). Track the farthest reachable index.
    """
    far = 0
    for i, x in enumerate(nums):
        if i > far:
            return False
        far = max(far, i + x)
    return True


def jump(nums: List[int]) -> int:
    """Minimum jumps to reach the last index (always reachable).

    jump([2,3,1,1,4]) -> 2
    Target: O(n). Greedy BFS-by-layers.
    """
    jumps = cur_end = far = 0
    for i in range(len(nums) - 1):
        far = max(far, i + nums[i])
        if i == cur_end:  # must jump now to go further
            jumps += 1
            cur_end = far
    return jumps


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    """Circular route: gas[i] fuel at station i, cost[i] fuel to reach i+1. Return the starting
    station index that completes the loop (unique), or -1.

    can_complete_circuit([1,2,3,4,5], [3,4,5,1,2]) -> 3
    Target: O(n).
    """
    if sum(gas) < sum(cost):
        return -1
    tank = start = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:  # can't start at or before i
            start, tank = i + 1, 0
    return start


def partition_labels(s: str) -> List[int]:
    """Split s into as many parts as possible so each letter appears in at most one part. Return part sizes.

    partition_labels("ababcbacadefegdehijhklij") -> [9,7,8]
    Target: O(n).
    """
    last = {c: i for i, c in enumerate(s)}
    res, start, end = [], 0, 0
    for i, c in enumerate(s):
        end = max(end, last[c])
        if i == end:
            res.append(end - start + 1)
            start = i + 1
    return res


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    """Minimum number of intervals to remove so the rest don't overlap ([1,2] and [2,3] don't overlap).

    erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]) -> 1
    Target: O(n log n). Sort by END time; keep what ends earliest.
    """
    end, removed = -inf, 0
    for s, e in sorted(intervals, key=lambda x: x[1]):
        if s >= end:
            end = e
        else:
            removed += 1
    return removed


def candy(ratings: List[int]) -> int:
    """Each child gets >= 1 candy; a child with a higher rating than a neighbour gets more than that neighbour.
    Minimum candies total.

    candy([1,0,2]) -> 5
    Target: O(n) with two passes (left->right, right->left).
    """
    n = len(ratings)
    c = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            c[i] = c[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            c[i] = max(c[i], c[i + 1] + 1)
    return sum(c)
