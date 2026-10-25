'Section 15 - Greedy Algorithms (your workspace).'


from typing import List


def max_sub_array(nums: List[int]) -> int:
    """Largest sum of a contiguous non-empty subarray (Kadane's algorithm).

    max_sub_array([-2,1,-3,4,-1,2,1,-5,4]) -> 6
    Target: O(n), O(1) space.
    """
    pass


def can_jump(nums: List[int]) -> bool:
    """nums[i] = max jump length from i. Starting at index 0, can you reach the last index?

    can_jump([2,3,1,1,4]) -> True ; can_jump([3,2,1,0,4]) -> False
    Target: O(n). Track the farthest reachable index.
    """
    pass


def jump(nums: List[int]) -> int:
    """Minimum jumps to reach the last index (always reachable).

    jump([2,3,1,1,4]) -> 2
    Target: O(n). Greedy BFS-by-layers.
    """
    pass


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    """Circular route: gas[i] fuel at station i, cost[i] fuel to reach i+1. Return the starting
    station index that completes the loop (unique), or -1.

    can_complete_circuit([1,2,3,4,5], [3,4,5,1,2]) -> 3
    Target: O(n).
    """
    pass


def partition_labels(s: str) -> List[int]:
    """Split s into as many parts as possible so each letter appears in at most one part. Return part sizes.

    partition_labels("ababcbacadefegdehijhklij") -> [9,7,8]
    Target: O(n).
    """
    pass


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    """Minimum number of intervals to remove so the rest don't overlap ([1,2] and [2,3] don't overlap).

    erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]) -> 1
    Target: O(n log n). Sort by END time; keep what ends earliest.
    """
    pass


def candy(ratings: List[int]) -> int:
    """Each child gets >= 1 candy; a child with a higher rating than a neighbour gets more than that neighbour.
    Minimum candies total.

    candy([1,0,2]) -> 5
    Target: O(n) with two passes (left->right, right->left).
    """
    pass
