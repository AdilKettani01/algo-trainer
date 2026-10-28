'Section 01 - Arrays & Hashing (your workspace).'


from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Return indices [i, j] (i != j) such that nums[i] + nums[j] == target.
    Exactly one valid pair exists.

    two_sum([2, 7, 11, 15], 9) -> [0, 1]
    Target: O(n) time, O(n) space.
    """

    seen = {}

    for i, num in nums:
        if target - num in seen:
            if target - num != seen[i]:
                return [seen[target-num], i]
        seen[num] = i
    pass


def contains_duplicate(nums: List[int]) -> bool:
    """Return True if any value appears at least twice.

    contains_duplicate([1, 2, 3, 1]) -> True
    Target: O(n) time.
    """

    seen = {}

    for i, num in enumerate(nums)   :
        if num in seen:
            return True
        seen[num] = i
    return False
    pass


def is_anagram(s: str, t: str) -> bool:
    """Return True if t is a rearrangement of s.

    is_anagram("anagram", "nagaram") -> True
    Target: O(n) time.
    """

    s_arr = list(s.lower())
    t_arr = list(t.lower())
    if (s_arr == t_arr):
        print("True")
        return True
    else:
        print("False")
        return False
    pass



def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Group words that are anagrams of each other (any group order).

    group_anagrams(["eat","tea","tan","ate","nat","bat"])
      -> [["eat","tea","ate"],["tan","nat"],["bat"]]
    Target: O(n * k log k) where k = longest word.
    """
    pass


def top_k_frequent(nums: List[int], k: int) -> List[int]:

    """Return the k most frequent values (any order).

    top_k_frequent([1,1,1,2,2,3], 2) -> [1, 2]
    Target: O(n) with bucket sort (O(n log k) with a heap is fine too).
    """
    d_list = {}
    
    # Filling up dict with num : count
    for i , num in enumerate(nums):
        if num in d_list:
            d_list[num] = d_list[num] + 1
        else:
            d_list[num] = 1
    #Fill bucket_list

    bucket_list = []
    for _ in range(len(nums) + 1):
        bucket_list.append([])  

    #Fill with proper and sorted val
    for num, count in d_list.items():
        bucket_list[count].append(num)




    result = []

    if (k > len(bucket_list)):
        print("k is out of bound of result, please choose smaller k value or diffrent list")
    else:
        for i in range(len(bucket_list) -1, -1 ,-1):
            if bucket_list[i] == []:
                continue    
            else:
                result.append(bucket_list[i])
            if len(result) == 2:
                break
                
    
    return result
    pass


def product_except_self(nums: List[int]) -> List[int]:
    """out[i] = product of every element except nums[i]. No division allowed.

    product_except_self([1,2,3,4]) -> [24,12,8,6]
    Target: O(n) time, O(1) extra space (besides output).
    """
    pass


def longest_consecutive(nums: List[int]) -> int:
    """Length of the longest run of consecutive integers (order in nums irrelevant).

    longest_consecutive([100,4,200,1,3,2]) -> 4   (1,2,3,4)
    Target: O(n) time.
    """
    pass
