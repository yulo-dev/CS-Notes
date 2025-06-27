from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Edge case: if there's only one or two nodes, all of them are valid roots
        if n <= 2:
            return [i for i in range(n)]

        # Step 1: Build the adjacency list and compute the degree of each node
        graph = defaultdict(list)
        degree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # Step 2: Initialize the first layer of leaves (nodes with degree == 1)
        leaves = deque([i for i in range(n) if degree[i] == 1])

        # Step 3: Trim the leaves layer by layer until 2 or fewer nodes remain
        remaining_nodes = n
        while remaining_nodes > 2:
            leaf_count = len(leaves)
            remaining_nodes -= leaf_count

            # Remove all current leaves
            for _ in range(leaf_count):
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1
                    # If neighbor becomes a leaf, add to the queue
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)

        # The remaining nodes are the centermost roots of the minimum height trees
        return list(leaves)
