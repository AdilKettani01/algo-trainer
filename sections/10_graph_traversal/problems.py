'Section 10 - Graph Traversal: DFS & BFS (your workspace).'


from typing import List


def num_islands(grid: List[List[str]]) -> int:
    """Count islands: groups of '1' connected up/down/left/right ('0' = water).

    Target: O(R*C). Flood-fill each unvisited land cell.
    """
    pass


def max_area_of_island(grid: List[List[int]]) -> int:
    """Size (cell count) of the largest island of 1s (4-directional). 0 if none.

    Target: O(R*C).
    """
    pass


def oranges_rotting(grid: List[List[int]]) -> int:
    """0 empty, 1 fresh, 2 rotten. Each minute rot spreads to 4-neighbours. Minutes until none fresh, or -1.

    [[2,1,1],[1,1,0],[0,1,1]] -> 4
    Target: O(R*C). Multi-source BFS (start with ALL rotten oranges in the queue).
    """
    pass


def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
    """Shortest clear path (cells with 0) from top-left to bottom-right moving in 8 directions.
    Return the number of cells on the path, or -1.

    [[0,1],[1,0]] -> 2
    Target: O(R*C). BFS gives shortest path in an unweighted graph.
    """
    pass


def is_bipartite(graph: List[List[int]]) -> bool:
    """graph[i] = neighbours of node i (undirected). Can nodes be 2-coloured so no edge joins same colours?

    Target: O(V + E). Hint: BFS/DFS colouring; handle disconnected graphs.
    """
    pass


def ladder_length(begin: str, end: str, word_list: List[str]) -> int:
    """Shortest transformation sequence begin -> end changing one letter at a time, every word in word_list.
    Return the number of words in the sequence (including begin), or 0.

    ladder_length("hit","cog",["hot","dot","dog","lot","log","cog"]) -> 5
    Target: BFS over an IMPLICIT graph (neighbours = one-letter changes).
    """
    pass
