'Section 12 - Backtracking (your workspace).'


from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """All subsets (the power set) of distinct integers, any order.

    subsets([1,2,3]) -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    Target: O(n * 2^n). Choose / don't choose each element.
    """
    pass


def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    """All UNIQUE subsets of an array that may contain duplicates.

    subsets_with_dup([1,2,2]) -> [[],[1],[1,2],[1,2,2],[2],[2,2]]
    Target: sort first, then skip equal values at the same recursion depth.
    """
    pass


def permutations(nums: List[int]) -> List[List[int]]:
    """All orderings of distinct integers.

    permutations([1,2,3]) -> 6 lists
    Target: O(n * n!).
    """
    pass


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """Distinct positive candidates, each reusable unlimited times. All UNIQUE combos summing to target.

    combination_sum([2,3,6,7], 7) -> [[2,2,3],[7]]
    """
    pass


def generate_parenthesis(n: int) -> List[str]:
    """All well-formed strings with n pairs of parentheses.

    generate_parenthesis(3) -> ["((()))","(()())","(())()","()(())","()()()"]
    Target: Catalan(n) outputs. Only add ')' when it won't over-close.
    """
    pass


def exist(board: List[List[str]], word: str) -> bool:
    """Is `word` traceable in the grid via adjacent (up/down/left/right) cells, each cell used once?

    Target: O(R*C*4^len). DFS with a visited mark you UNDO on the way back.
    """
    pass


def total_n_queens(n: int) -> int:
    """Number of ways to place n queens on an n x n board so none attack each other.

    total_n_queens(4) -> 2 ; total_n_queens(8) -> 92
    Target: track used columns and both diagonals in sets (O(1) checks).
    """
    pass
