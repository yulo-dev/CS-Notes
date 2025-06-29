# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []  # Empty tree → return empty list

        result = []              # Final list to store each level's values
        queue = deque([root])    # BFS queue starting with root node

        while queue:
            level_size = len(queue)  # Number of nodes in this level
            level = []               # To store node values at current level

            for _ in range(level_size):
                node = queue.popleft()     # Pop from queue (FIFO)
                level.append(node.val)     # Add current node's value to level list

                if node.left:
                    queue.append(node.left)   # Add left child to queue
                if node.right:
                    queue.append(node.right)  # Add right child to queue

            result.append(level)  # Store current level into final result

        return result
