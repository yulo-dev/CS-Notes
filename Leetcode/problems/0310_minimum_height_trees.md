# Leetcode 0310 - Minimum Height Trees

## ☀️ UMPIRE
- **Understand**: Return all root labels that would create a minimum height tree from a given undirected tree.
- **Match**: Graph problem; connected undirected tree with `n` nodes and `n-1` edges → suitable for multi-source BFS.
- **Plan**: 
  1. Handle edge case: if `n <= 2`, return all nodes directly.
  2. Build graph and degree array.
  3. Use deque to enqueue all current leaves (degree == 1).
  4. Trim leaves layer by layer until 1 or 2 nodes remain.
  5. Return remaining nodes as result.
- **Implement**: Use adjacency list and degree array to simulate leaf trimming (topological BFS).
- **Review**: Tree centers are always 1 or 2 nodes that lie at the middle of the longest path (diameter).
- **Evaluate**: Time `O(n)`, Space `O(n)`.

## ☀️ Metadata
- **Appears In**: Grind75
- **Pattern**: Topological Trim / Tree Center via BFS
- **Data Structure**: Adjacency List, Degree Array, Queue
- **Algorithm**: Multi-source BFS
- **Tags**: Graph, Tree, Topological Sort, BFS


## ☀️ Solution Code

```python
from collections import defaultdict, deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        graph = defaultdict(list)
        degree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        leaves = deque([i for i in range(n) if degree[i] == 1])

        remaining_nodes = n
        while remaining_nodes > 2:
            leaf_count = len(leaves)
            remaining_nodes -= leaf_count

            for _ in range(leaf_count):
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)

        return list(leaves)
```

## ☀️ Trace

```
Input: n = 6, edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]
Initial degrees: [3,1,1,2,2,1]
Initial leaves: [1,2,5]

Round 1: remove [1,2,5]
  → update degree[0] = 1, degree[4] = 1
  → new leaves = [0,4]

Round 2: remove [0,4]
  → update degree[3] = 1
  → new leaf = [3]

Remaining node = 3 → return [3]
```

## ☀️ Line-by-line Typing Script

- I check if n <= 2, and directly return all nodes as potential roots.
- I build a graph using an adjacency list and track each node’s degree.
- For each edge, I record neighbors in both directions and increment degrees.
- Then I initialize the leaves list: nodes with degree == 1.
- I begin a while loop that continues until ≤2 nodes remain.
- Each round, I remove all current leaves, decrement neighbors’ degrees.
- If a neighbor becomes a new leaf (degree == 1), I add it to the queue.
- Finally, the remaining 1–2 nodes are the centers of the minimum height tree.

## ☀️ Evaluate

**Time Complexity:** `O(n)`  
- Each node and edge is visited once during graph build and BFS trim

**Space Complexity:** `O(n)`  
- Adjacency list: O(n)  
- Degree array: O(n)  
- Queue of leaves: O(n) in worst case


## ☀️ Pattern

- Multi-source BFS
- Topological sort (inward)
- Tree center detection (diameter middle)
