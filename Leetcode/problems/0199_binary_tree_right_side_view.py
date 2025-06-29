# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            # Base case: if the node is null, return
            if not node:
                return
            
            # If this is the first time we've reached this depth,
            # then this node is the rightmost node at this level
            if depth == len(res):
                res.append(node.val)

            # Visit right child first to ensure rightmost nodes are visited first
            dfs(node.right, depth + 1)

            # Then visit left child
            dfs(node.left, depth + 1)

        # Start DFS from root at depth 0
        dfs(root, 0)
        return res
