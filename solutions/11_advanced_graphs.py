"""Section 11 - Advanced Graphs: Topo Sort, Union-Find, Dijkstra, MST, Bellman-Ford (reference solutions)."""
import heapq
from collections import defaultdict, deque
from math import inf
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """prerequisites[i] = [a, b] means 'take b before a'. Can all courses be finished (no cycle)?

    can_finish(2, [[1,0]]) -> True ; can_finish(2, [[1,0],[0,1]]) -> False
    Target: O(V + E). Kahn's algorithm (topological sort by in-degree).
    """
    return len(find_order(num_courses, prerequisites)) == num_courses


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    """Return one valid order to take all courses, or [] if impossible.

    Target: O(V + E).
    """
    adj, indeg = defaultdict(list), [0] * num_courses
    for a, b in prerequisites:
        adj[b].append(a)
        indeg[a] += 1
    q = deque(i for i in range(num_courses) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == num_courses else []


def count_components(n: int, edges: List[List[int]]) -> int:
    """Number of connected components in an undirected graph with n nodes (0..n-1).

    count_components(5, [[0,1],[1,2],[3,4]]) -> 2
    Target: ~O(E * alpha(n)) with Union-Find.
    """
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # path compression (halving)
            x = parent[x]
        return x

    comps = n
    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
            comps -= 1
    return comps


def find_redundant_connection(edges: List[List[int]]) -> List[int]:
    """A tree with n nodes (1..n) got ONE extra edge. Return the edge that can be removed
    (if several, the one appearing last in the input).

    find_redundant_connection([[1,2],[1,3],[2,3]]) -> [2,3]
    Target: Union-Find: the first edge joining two already-connected nodes.
    """
    parent = list(range(len(edges) + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return [a, b]
        parent[ra] = rb


def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    """times[i] = [u, v, w]: signal from u to v takes w. Nodes 1..n. Time for ALL nodes to
    receive a signal sent from k, or -1.

    network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2) -> 2
    Target: O(E log V). Dijkstra.
    """
    adj = defaultdict(list)
    for u, v, w in times:
        adj[u].append((v, w))
    dist = {}
    heap = [(0, k)]
    while heap:
        d, u = heapq.heappop(heap)
        if u in dist:
            continue
        dist[u] = d
        for v, w in adj[u]:
            if v not in dist:
                heapq.heappush(heap, (d + w, v))
    return max(dist.values()) if len(dist) == n else -1


def min_cost_connect_points(points: List[List[int]]) -> int:
    """Connect all points with the minimum total Manhattan distance (|x1-x2|+|y1-y2|). Minimum spanning tree.

    min_cost_connect_points([[0,0],[2,2],[3,10],[5,2],[7,0]]) -> 20
    Target: O(n^2) Prim, or O(E log E) Kruskal.
    """
    n = len(points)
    best = [inf] * n  # cheapest edge connecting each node to the tree
    best[0], used, total = 0, [False] * n, 0
    for _ in range(n):
        u = min((i for i in range(n) if not used[i]), key=lambda i: best[i])
        used[u] = True
        total += best[u]
        for v in range(n):
            if not used[v]:
                d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                best[v] = min(best[v], d)
    return total


def find_cheapest_price(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    """flights[i] = [from, to, price]. Cheapest price src -> dst with at most k STOPS, or -1.

    find_cheapest_price(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1) -> 200
    Target: O(k * E). Bellman-Ford limited to k+1 edges.
    """
    prices = [inf] * n
    prices[src] = 0
    for _ in range(k + 1):
        nxt = prices[:]  # relax using LAST round's values only
        for u, v, w in flights:
            if prices[u] + w < nxt[v]:
                nxt[v] = prices[u] + w
        prices = nxt
    return -1 if prices[dst] == inf else prices[dst]
