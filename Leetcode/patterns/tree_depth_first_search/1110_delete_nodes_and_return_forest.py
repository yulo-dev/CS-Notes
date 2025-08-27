# LeetCode 1110: Delete Nodes and Return Forest
# Given the root of a binary tree, each node in the tree has a distinct value.
# After deleting all nodes with values in to_delete, we are left with a forest (a disjoint union of trees).
# Return the roots of the trees in the remaining forest. You may return the result in any order.

from typing import Optional, List

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1: Brute Force - Multiple Passes with Tree Reconstruction
# Time: O(n * k) → k passes over tree, each pass O(n) where k = len(to_delete)
# Space: O(n) → Store intermediate tree structures and recursion stack
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def clone_tree(node):
            """Create a deep copy of the tree"""
            if not node:
                return None
            new_node = TreeNode(node.val)
            new_node.left = clone_tree(node.left)
            new_node.right = clone_tree(node.right)
            return new_node
        
        def delete_node(tree_root, target):
            """Delete target node and return new roots created"""
            if not tree_root:
                return []
            
            if tree_root.val == target:
                # Root is deleted, children become new roots
                new_roots = []
                if tree_root.left:
                    new_roots.append(tree_root.left)
                if tree_root.right:
                    new_roots.append(tree_root.right)
                return new_roots
            
            # Search and delete in subtrees
            new_roots = []
            
            # Check left child
            if tree_root.left and tree_root.left.val == target:
                deleted_node = tree_root.left
                tree_root.left = None
                if deleted_node.left:
                    new_roots.append(deleted_node.left)
                if deleted_node.right:
                    new_roots.append(deleted_node.right)
            else:
                new_roots.extend(delete_node(tree_root.left, target))
            
            # Check right child
            if tree_root.right and tree_root.right.val == target:
                deleted_node = tree_root.right
                tree_root.right = None
                if deleted_node.left:
                    new_roots.append(deleted_node.left)
                if deleted_node.right:
                    new_roots.append(deleted_node.right)
            else:
                new_roots.extend(delete_node(tree_root.right, target))
            
            return new_roots
        
        # Start with original root
        current_roots = [root]
        
        # Delete each target value one by one
        for target in to_delete:
            next_roots = []
            for tree_root in current_roots:
                if tree_root.val == target:
                    # This root is deleted, add its children
                    if tree_root.left:
                        next_roots.append(tree_root.left)
                    if tree_root.right:
                        next_roots.append(tree_root.right)
                else:
                    # Keep this root and apply deletion
                    new_roots = delete_node(tree_root, target)
                    next_roots.append(tree_root)
                    next_roots.extend(new_roots)
            current_roots = next_roots
        
        return current_roots

# Solution 2: Single-Pass DFS with Set Lookup (Classic Solution)
# Time: O(n) → Visit each node exactly once
# Space: O(h + k) → Recursion stack depth + set storage for to_delete values
class Solution2:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        dels = set(to_delete)
        forest = []

        def dfs(node, is_root):
            if not node:
                return None

            # Recursively process children - they become roots if current node is deleted
            node.left = dfs(node.left, node.val in dels)
            node.right = dfs(node.right, node.val in dels)

            # If current node should be deleted, return None to disconnect it
            if node.val in dels:
                return None

            # If current node is not deleted and is a root, add to forest
            if is_root:
                forest.append(node)

            return node

        dfs(root, True)
        return forest

# Solution 3: Advanced - Post-order with Parent Tracking
# Time: O(n) → Visit each node exactly once
# Space: O(h + k) → Recursion stack depth + set storage
class Solution3:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        result = []
        
        def postorder(node, parent, is_left_child):
            """
            Post-order traversal with explicit parent tracking
            Process children first, then current node
            """
            if not node:
                return
            
            # Process children first (post-order)
            postorder(node.left, node, True)
            postorder(node.right, node, False)
            
            # Process current node after children are handled
            if node.val in to_delete_set:
                # Current node will be deleted
                # Disconnect from parent
                if parent:
                    if is_left_child:
                        parent.left = None
                    else:
                        parent.right = None
                
                # Add non-deleted children as new roots
                if node.left:
                    result.append(node.left)
                if node.right:
                    result.append(node.right)
            elif not parent:  # Root node that is not deleted
                result.append(node)
        
        postorder(root, None, False)
        return result

# Test function
def test_solutions():
    def print_tree_values(roots):
        """Helper function to print tree values for verification"""
        def get_values(node):
            if not node:
                return []
            values = [node.val]
            values.extend(get_values(node.left))
            values.extend(get_values(node.right))
            return values
        
        result = []
        for root in roots:
            result.append(sorted(get_values(root)))
        return sorted(result)
    
    # Create test tree:       1
    #                        / \
    #                       2   3
    #                      / \   \
    #                     4   5   6
    #                        /
    #                       7
    # to_delete = [3, 5]
    # Expected forest: [[1,2,4], [6], [7]]
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.right.left = TreeNode(7)
    
    to_delete = [3, 5]
    
    sol2 = Solution2()
    sol3 = Solution3()
    
    # Create separate trees for each solution (since they modify the tree)
    def create_test_tree():
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
        root.left.right.left = TreeNode(7)
        return root
    
    result2 = sol2.delNodes(create_test_tree(), to_delete)
    result3 = sol3.delNodes(create_test_tree(), to_delete)
    
    print(f"Single-pass DFS: {print_tree_values(result2)}")
    print(f"Post-order: {print_tree_values(result3)}")
    
    # Test edge cases
    # Single node deletion
    single_root = TreeNode(1)
    result_single = sol2.delNodes(single_root, [1])
    print(f"Delete root only: {len(result_single)} trees")  # Expected: 0
    
    # No deletions
    no_del_root = TreeNode(1)
    no_del_root.left = TreeNode(2)
    result_no_del = sol2.delNodes(no_del_root, [])
    print(f"No deletions: {print_tree_values(result_no_del)}")  # Expected: [[1, 2]]

# Strategy:
# 1. Start with Solution 1 (Brute Force) 
# 2. Optimize to Solution 2 (Single-pass DFS) 
# 3. If time permits, mention Solution 3 (Post-order) as alternative approach
#
# Key insight: Use DFS to process deletions and identify new roots in single pass
# Solution 2 is preferred:
# - Optimal O(n) time complexity with single tree traversal
# - Clean and concise logic: process children first, then decide on current node
# - Efficient inline computation of is_root for children (node.val in dels)
# - Natural post-order processing that handles deletions elegantly
# - Easy to explain: "process children, then delete current if needed, add roots to forest"
