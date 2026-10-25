# 11 - Advanced Graphs

## Topological sort (DAGs)
Order nodes so every edge `u → v` has `u` before `v` (course prerequisites, build order).
**Kahn's algorithm**: compute in-degrees, queue all with 0, pop → append to order → decrement neighbours' in-degree → enqueue newly-zero nodes. If `len(order) < n` ⇒ **cycle**. O(V+E).

## Union-Find (Disjoint Set Union)
Maintains groups with near-O(1) `find`/`union`.
```python
parent = list(range(n))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]   # path compression
        x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb: return False           # already connected -> this edge makes a cycle
    parent[ra] = rb; return True
```
Uses: connected components, detect cycle in undirected graph, redundant connection, Kruskal's MST. (Optimise further with union by rank/size.)

## Dijkstra (shortest paths, non-negative weights)
Min-heap of `(dist, node)`. Pop the closest unfinalised node, relax its edges, push improvements. O((V+E) log V). **Fails with negative edges.**
```python
heap = [(0, src)]; dist = {}
while heap:
    d, u = heappop(heap)
    if u in dist: continue          # stale entry
    dist[u] = d
    for v, w in adj[u]:
        if v not in dist: heappush(heap, (d + w, v))
```

## Bellman-Ford
Relax **all** edges `V-1` times; handles negative edges and detects negative cycles (an extra round still improves). With "at most k stops": run exactly `k+1` rounds and relax from a **copy** of last round's distances. O(V·E).

## Minimum Spanning Tree
Cheapest set of edges connecting all nodes.
- **Kruskal**: sort edges, add if it joins two different components (Union-Find).
- **Prim**: grow from one node, always add the cheapest edge leaving the tree (heap, or O(n²) array for dense graphs - used in `min_cost_connect_points`).

## Which tool?
| Need | Use |
|---|---|
| Unweighted shortest path | BFS |
| Non-negative weights | Dijkstra |
| Negative weights / ≤k edges | Bellman-Ford |
| All pairs (small V) | Floyd-Warshall O(V³) |
| Ordering / cycle in directed graph | Topological sort |
| Dynamic connectivity, undirected cycles | Union-Find |
| Cheapest connection | MST |

**Practice:** `can_finish`, `find_order`, `count_components`, `find_redundant_connection`, `network_delay_time`, `min_cost_connect_points`, `find_cheapest_price`.
