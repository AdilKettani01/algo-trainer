'Section 11 - Advanced Graphs: Topo Sort, Union-Find, Dijkstra, MST, Bellman-Ford (your workspace).'


from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """prerequisites[i] = [a, b] means 'take b before a'. Can all courses be finished (no cycle)?

    can_finish(2, [[1,0]]) -> True ; can_finish(2, [[1,0],[0,1]]) -> False
    Target: O(V + E). Kahn's algorithm (topological sort by in-degree).
    """
    pass


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    """Return one valid order to take all courses, or [] if impossible.

    Target: O(V + E).
    """
    pass


def count_components(n: int, edges: List[List[int]]) -> int:
    """Number of connected components in an undirected graph with n nodes (0..n-1).

    count_components(5, [[0,1],[1,2],[3,4]]) -> 2
    Target: ~O(E * alpha(n)) with Union-Find.
    """
    pass


def find_redundant_connection(edges: List[List[int]]) -> List[int]:
    """A tree with n nodes (1..n) got ONE extra edge. Return the edge that can be removed
    (if several, the one appearing last in the input).

    find_redundant_connection([[1,2],[1,3],[2,3]]) -> [2,3]
    Target: Union-Find: the first edge joining two already-connected nodes.
    """
    pass


def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    """times[i] = [u, v, w]: signal from u to v takes w. Nodes 1..n. Time for ALL nodes to
    receive a signal sent from k, or -1.

    network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2) -> 2
    Target: O(E log V). Dijkstra.
    """
    pass


def min_cost_connect_points(points: List[List[int]]) -> int:
    """Connect all points with the minimum total Manhattan distance (|x1-x2|+|y1-y2|). Minimum spanning tree.

    min_cost_connect_points([[0,0],[2,2],[3,10],[5,2],[7,0]]) -> 20
    Target: O(n^2) Prim, or O(E log E) Kruskal.
    """
    pass


def find_cheapest_price(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    """flights[i] = [from, to, price]. Cheapest price src -> dst with at most k STOPS, or -1.

    find_cheapest_price(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1) -> 200
    Target: O(k * E). Bellman-Ford limited to k+1 edges.
    """
    pass
