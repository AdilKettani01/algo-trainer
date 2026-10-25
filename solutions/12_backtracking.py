"""Section 12 - Backtracking (reference solutions)."""
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """All subsets (the power set) of distinct integers, any order.

    subsets([1,2,3]) -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    Target: O(n * 2^n). Choose / don't choose each element.
    """
    res, path = [], []

    def go(i):
        if i == len(nums):
            res.append(path[:])
            return
        path.append(nums[i])  # choose
        go(i + 1)
        path.pop()  # un-choose (backtrack)
        go(i + 1)  # skip

    go(0)
    return res


def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    """All UNIQUE subsets of an array that may contain duplicates.

    subsets_with_dup([1,2,2]) -> [[],[1],[1,2],[1,2,2],[2],[2,2]]
    Target: sort first, then skip equal values at the same recursion depth.
    """
    nums = sorted(nums)
    res, path = [], []

    def go(start):
        res.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            go(i + 1)
            path.pop()

    go(0)
    return res


def permutations(nums: List[int]) -> List[List[int]]:
    """All orderings of distinct integers.

    permutations([1,2,3]) -> 6 lists
    Target: O(n * n!).
    """
    res, path, used = [], [], [False] * len(nums)

    def go():
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                go()
                path.pop()
                used[i] = False

    go()
    return res


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """Distinct positive candidates, each reusable unlimited times. All UNIQUE combos summing to target.

    combination_sum([2,3,6,7], 7) -> [[2,2,3],[7]]
    """
    res, path = [], []

    def go(start, remain):
        if remain == 0:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            c = candidates[i]
            if c <= remain:
                path.append(c)
                go(i, remain - c)  # i (not i+1): reuse allowed; start index avoids permutations
                path.pop()

    go(0, target)
    return res


def generate_parenthesis(n: int) -> List[str]:
    """All well-formed strings with n pairs of parentheses.

    generate_parenthesis(3) -> ["((()))","(()())","(())()","()(())","()()()"]
    Target: Catalan(n) outputs. Only add ')' when it won't over-close.
    """
    res = []

    def go(cur, opened, closed):
        if len(cur) == 2 * n:
            res.append(cur)
            return
        if opened < n:
            go(cur + "(", opened + 1, closed)
        if closed < opened:
            go(cur + ")", opened, closed + 1)

    go("", 0, 0)
    return res


def exist(board: List[List[str]], word: str) -> bool:
    """Is `word` traceable in the grid via adjacent (up/down/left/right) cells, each cell used once?

    Target: O(R*C*4^len). DFS with a visited mark you UNDO on the way back.
    """
    R, C = len(board), len(board[0])

    def go(r, c, i):
        if i == len(word):
            return True
        if not (0 <= r < R and 0 <= c < C) or board[r][c] != word[i]:
            return False
        tmp, board[r][c] = board[r][c], "#"
        found = any(go(r + dr, c + dc, i + 1) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        board[r][c] = tmp  # backtrack
        return found

    return any(go(r, c, 0) for r in range(R) for c in range(C))


def total_n_queens(n: int) -> int:
    """Number of ways to place n queens on an n x n board so none attack each other.

    total_n_queens(4) -> 2 ; total_n_queens(8) -> 92
    Target: track used columns and both diagonals in sets (O(1) checks).
    """
    cols, diag, anti = set(), set(), set()

    def go(r):
        if r == n:
            return 1
        count = 0
        for c in range(n):
            if c in cols or (r - c) in diag or (r + c) in anti:
                continue
            cols.add(c); diag.add(r - c); anti.add(r + c)
            count += go(r + 1)
            cols.remove(c); diag.remove(r - c); anti.remove(r + c)
        return count

    return go(0)
