# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize counter and result container
        self.k = k                # Counts how many nodes we have left to visit
        self.res = None           # Stores the kth smallest value once found

        # Helper function to perform in-order traversal
        def inorder(node):
            if not node:
                return  # Base case: empty subtree, do nothing

            inorder(node.left)  # Recurse into left subtree (smaller values first)

            self.k -= 1         # Visit current node: decrement k
            if self.k == 0:     # If this is the kth node visited
                self.res = node.val  # Record its value as the answer
                return          # Early return to stop further traversal

            inorder(node.right) # Recurse into right subtree (larger values)

        # Start traversal from the root
        inorder(root)
        return self.res  # Return the result found during traversal
