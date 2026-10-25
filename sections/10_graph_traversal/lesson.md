# 10 - Graph Traversal: DFS & BFS

## Representing graphs
- **Adjacency list** `{u: [v, ...]}` - default, O(V+E).
- **Grid** - cells are nodes; neighbours via `DIRS = [(1,0),(-1,0),(0,1),(0,-1)]`.
- **Implicit graph** - nodes are states (words, puzzle boards); neighbours generated on the fly.

## DFS (stack or recursion)
Go deep, backtrack. Use for: connected components, flood fill, cycle detection, path existence.
```python
def dfs(r, c):
    if out_of_bounds or water or (r, c) in seen: return
    seen.add((r, c))
    for dr, dc in DIRS: dfs(r + dr, c + dc)
```
Count islands = number of times you *start* a fresh DFS. For big grids use an explicit stack (Python recursion limit ≈ 1000).

## BFS (queue)
Visit in rings of distance → **shortest path in an unweighted graph**.
```python
q = deque([(start, 0)]); seen = {start}
while q:
    node, d = q.popleft()
    for nb in neighbours(node):
        if nb not in seen:
            seen.add(nb); q.append((nb, d + 1))
```
- **Mark visited when you enqueue**, not when you dequeue (else duplicates explode).
- **Multi-source BFS**: put *all* sources in the queue at distance 0 (rotting oranges, walls & gates).
- **Level by level**: `for _ in range(len(q))` per minute/step.
- **Implicit graph BFS**: word ladder - neighbours are one-letter changes.

## Bipartite check
2-colour with BFS/DFS: a neighbour with the *same* colour ⇒ odd cycle ⇒ not bipartite. Loop over all start nodes (graph may be disconnected).

## Complexity
O(V + E) time, O(V) space. Grid: O(R·C).

## Pitfalls
- Don't forget `seen` → infinite loops.
- Diagonal moves = 8 directions.
- Return distance in *nodes* vs *edges* carefully (path length 1 for a single cell).

**Practice:** `num_islands`, `max_area_of_island`, `oranges_rotting`, `shortest_path_binary_matrix`, `is_bipartite`, `ladder_length`.
