"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        oldToNew = {}  # Dictionary to store mapping: original node -> copied node

        def dfs(node):
            # If the node has already been copied, return the copied version
            if node in oldToNew:
                return oldToNew[node]

            # Step 1: Clone the current node (only value, no neighbors yet)
            copy = Node(node.val)
            # Step 2: Save this copy in the dictionary before processing neighbors
            oldToNew[node] = copy

            # Step 3: Recursively clone and append all neighbors
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        # Start DFS from the given node
        return dfs(node) if node else None # If the input graph is empty, return None
