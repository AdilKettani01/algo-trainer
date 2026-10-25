"""Section 02 - Two Pointers (reference solutions)."""
from typing import List


def is_palindrome(s: str) -> bool:
    """True if s is a palindrome ignoring case and non-alphanumerics.

    is_palindrome("A man, a plan, a canal: Panama") -> True
    Target: O(n) time, O(1) space.
    """
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    """numbers is sorted ascending. Return 1-indexed [i, j] with numbers[i]+numbers[j]==target.

    two_sum_sorted([2,7,11,15], 9) -> [1, 2]
    Target: O(n) time, O(1) space.
    """
    l, r = 0, len(numbers) - 1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l + 1, r + 1]
        if s < target:
            l += 1  # need a bigger sum
        else:
            r -= 1  # need a smaller sum


def three_sum(nums: List[int]) -> List[List[int]]:
    """All UNIQUE triplets [a,b,c] with a+b+c == 0.

    three_sum([-1,0,1,2,-1,-4]) -> [[-1,-1,2],[-1,0,1]]
    Target: O(n^2) time.
    """
    nums = sorted(nums)
    res = []
    for i, a in enumerate(nums):
        if a > 0:
            break
        if i and a == nums[i - 1]:  # skip duplicate anchors
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = a + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
    return res


def max_area(height: List[int]) -> int:
    """Two vertical lines + the x-axis form a container. Return max water it can hold.

    max_area([1,8,6,2,5,4,8,3,7]) -> 49
    Target: O(n) time.
    """
    l, r, best = 0, len(height) - 1, 0
    while l < r:
        best = max(best, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:  # the shorter wall limits us; move it
            l += 1
        else:
            r -= 1
    return best


def trap(height: List[int]) -> int:
    """Rain water trapped between bars of the given heights.

    trap([0,1,0,2,1,0,1,3,2,1,2,1]) -> 6
    Target: O(n) time, O(1) space.
    """
    l, r = 0, len(height) - 1
    lmax = rmax = water = 0
    while l < r:
        if height[l] < height[r]:
            lmax = max(lmax, height[l])
            water += lmax - height[l]
            l += 1
        else:
            rmax = max(rmax, height[r])
            water += rmax - height[r]
            r -= 1
    return water


def remove_duplicates(nums: List[int]) -> int:
    """nums is sorted. Remove duplicates IN PLACE; return k = count of unique values.
    The first k slots of nums must hold the unique values in order.

    nums=[0,0,1,1,1,2] -> returns 3, nums[:3] == [0,1,2]
    Target: O(n) time, O(1) space (slow/fast pointers).
    """
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
