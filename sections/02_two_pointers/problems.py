'Section 02 - Two Pointers (your workspace).'


from typing import List


def is_palindrome(s: str) -> bool:
    """True if s is a palindrome ignoring case and non-alphanumerics.

    is_palindrome("A man, a plan, a canal: Panama") -> True
    Target: O(n) time, O(1) space.
    """
    pass


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    """numbers is sorted ascending. Return 1-indexed [i, j] with numbers[i]+numbers[j]==target.

    two_sum_sorted([2,7,11,15], 9) -> [1, 2]
    Target: O(n) time, O(1) space.
    """
    pass


def three_sum(nums: List[int]) -> List[List[int]]:
    """All UNIQUE triplets [a,b,c] with a+b+c == 0.

    three_sum([-1,0,1,2,-1,-4]) -> [[-1,-1,2],[-1,0,1]]
    Target: O(n^2) time.
    """
    pass


def max_area(height: List[int]) -> int:
    """Two vertical lines + the x-axis form a container. Return max water it can hold.

    max_area([1,8,6,2,5,4,8,3,7]) -> 49
    Target: O(n) time.
    """
    pass


def trap(height: List[int]) -> int:
    """Rain water trapped between bars of the given heights.

    trap([0,1,0,2,1,0,1,3,2,1,2,1]) -> 6
    Target: O(n) time, O(1) space.
    """
    pass


def remove_duplicates(nums: List[int]) -> int:
    """nums is sorted. Remove duplicates IN PLACE; return k = count of unique values.
    The first k slots of nums must hold the unique values in order.

    nums=[0,0,1,1,1,2] -> returns 3, nums[:3] == [0,1,2]
    Target: O(n) time, O(1) space (slow/fast pointers).
    """
    pass
