# first version:
# time complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Step 1: Create a hash map to store the index of each value in inorder for quick lookup
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        # Recursive helper function to build the tree
        def helper(pre_left: int, pre_right: int, in_left: int, in_right: int) -> Optional[TreeNode]:
            # Base case: if the current subtree range is invalid, return None
            if pre_left > pre_right:
                return None

            # The root of the current subtree is the first element in the preorder range
            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            # Find the index of the root in the inorder list
            in_root_idx = inorder_map[root_val]

            # Calculate the size of the left subtree
            left_size = in_root_idx - in_left

            # Recursively build the left subtree using the corresponding preorder and inorder ranges
            root.left = helper(
                pre_left + 1,                    # Left subtree in preorder starts after root
                pre_left + left_size,            # Ends at root + left_size
                in_left,                         # Left boundary in inorder
                in_root_idx - 1                  # Ends just before root in inorder
            )

            # Recursively build the right subtree
            root.right = helper(
                pre_left + left_size + 1,        # Right subtree in preorder starts after left subtree
                pre_right,                       # Ends at current preorder boundary
                in_root_idx + 1,                 # Starts just after root in inorder
                in_right                         # Ends at current inorder boundary
            )

            # Return the root node with left and right subtrees connected
            return root

        # Call the helper function with the full range of preorder and inorder indices
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)




# second version:
# time complexity: O(n²)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: if either list is empty, return None (no subtree)
        if not preorder or not inorder:
            return None

        # The first value in preorder is always the root of the current subtree
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Find the index of root in the inorder list
        # This splits the inorder list into left and right subtrees
        mid = inorder.index(root_val)

        # Build left subtree recursively
        # preorder[1:mid+1] corresponds to left subtree elements
        # inorder[:mid] contains all nodes in the left subtree
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])

        # Build right subtree recursively
        # preorder[mid+1:] corresponds to right subtree elements
        # inorder[mid+1:] contains all nodes in the right subtree
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # Return the constructed root node
        return root
