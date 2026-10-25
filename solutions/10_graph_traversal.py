"""Section 10 - Graph Traversal: DFS & BFS (reference solutions)."""
from collections import deque
from typing import List

DIRS4 = ((1, 0), (-1, 0), (0, 1), (0, -1))


def num_islands(grid: List[List[str]]) -> int:
    """Count islands: groups of '1' connected up/down/left/right ('0' = water).

    Target: O(R*C). Flood-fill each unvisited land cell.
    """
    if not grid:
        return 0
    R, C, seen, count = len(grid), len(grid[0]), set(), 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "1" and (r, c) not in seen:
                count += 1
                seen.add((r, c))
                stack = [(r, c)]
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in DIRS4:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == "1" and (nr, nc) not in seen:
                            seen.add((nr, nc))
                            stack.append((nr, nc))
    return count


def max_area_of_island(grid: List[List[int]]) -> int:
    """Size (cell count) of the largest island of 1s (4-directional). 0 if none.

    Target: O(R*C).
    """
    R, C, seen, best = len(grid), len(grid[0]), set(), 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1 and (r, c) not in seen:
                seen.add((r, c))
                stack, size = [(r, c)], 0
                while stack:
                    cr, cc = stack.pop()
                    size += 1
                    for dr, dc in DIRS4:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1 and (nr, nc) not in seen:
                            seen.add((nr, nc))
                            stack.append((nr, nc))
                best = max(best, size)
    return best


def oranges_rotting(grid: List[List[int]]) -> int:
    """0 empty, 1 fresh, 2 rotten. Each minute rot spreads to 4-neighbours. Minutes until none fresh, or -1.

    [[2,1,1],[1,1,0],[0,1,1]] -> 4
    Target: O(R*C). Multi-source BFS (start with ALL rotten oranges in the queue).
    """
    grid = [row[:] for row in grid]
    R, C, q, fresh = len(grid), len(grid[0]), deque(), 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 2:
                q.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
    minutes = 0
    while q and fresh:
        for _ in range(len(q)):  # one BFS layer = one minute
            r, c = q.popleft()
            for dr, dc in DIRS4:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
        minutes += 1
    return -1 if fresh else minutes


def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
    """Shortest clear path (cells with 0) from top-left to bottom-right moving in 8 directions.
    Return the number of cells on the path, or -1.

    [[0,1],[1,0]] -> 2
    Target: O(R*C). BFS gives shortest path in an unweighted graph.
    """
    n = len(grid)
    if grid[0][0] or grid[-1][-1]:
        return -1
    q, seen = deque([(0, 0, 1)]), {(0, 0)}
    while q:
        r, c, d = q.popleft()
        if (r, c) == (n - 1, n - 1):
            return d
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not grid[nr][nc] and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    q.append((nr, nc, d + 1))
    return -1


def is_bipartite(graph: List[List[int]]) -> bool:
    """graph[i] = neighbours of node i (undirected). Can nodes be 2-coloured so no edge joins same colours?

    Target: O(V + E). Hint: BFS/DFS colouring; handle disconnected graphs.
    """
    color = {}
    for start in range(len(graph)):
        if start in color:
            continue
        color[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in graph[u]:
                if v not in color:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False
    return True


def ladder_length(begin: str, end: str, word_list: List[str]) -> int:
    """Shortest transformation sequence begin -> end changing one letter at a time, every word in word_list.
    Return the number of words in the sequence (including begin), or 0.

    ladder_length("hit","cog",["hot","dot","dog","lot","log","cog"]) -> 5
    Target: BFS over an IMPLICIT graph (neighbours = one-letter changes).
    """
    words = set(word_list)
    if end not in words:
        return 0
    q, seen = deque([(begin, 1)]), {begin}
    while q:
        w, d = q.popleft()
        if w == end:
            return d
        for i in range(len(w)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                nw = w[:i] + ch + w[i + 1:]
                if nw in words and nw not in seen:
                    seen.add(nw)
                    q.append((nw, d + 1))
    return 0
