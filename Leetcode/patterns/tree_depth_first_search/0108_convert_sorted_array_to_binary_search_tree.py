# LeetCode 108: Convert Sorted Array to Binary Search Tree
# Given an integer array nums where the elements are sorted in ascending order, 
# convert it to a height-balanced binary search tree.
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees 
# of every node never differs by more than one.

from typing import Optional, List

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1: Brute Force - Recursive with Array Slicing
# Time: O(n log n) → O(n) for each level * O(log n) levels, plus array slicing overhead
# Space: O(n log n) → Array slicing creates new arrays at each recursive call
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        # Find middle element as root to ensure balance
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        
        # Recursively build left and right subtrees with array slicing
        root.left = self.sortedArrayToBST(nums[:mid])      # Left half
        root.right = self.sortedArrayToBST(nums[mid+1:])   # Right half
        
        return root

# Solution 2: Optimized Recursive with Index Pointers (Classic Interview Solution)
# Time: O(n) → Visit each element exactly once to create nodes
# Space: O(log n) → Recursion stack depth for balanced tree
# ★ This is the classic interview solution ★
class Solution2:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            # Base case: no elements to process
            if left > right:
                return None
            
            # Choose middle element as root to maintain balance
            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            
            # Recursively build left and right subtrees
            root.left = build(left, mid - 1)      # Left half
            root.right = build(mid + 1, right)    # Right half
            
            return root
        
        return build(0, len(nums) - 1)

# Solution 3: Advanced - Iterative with Stack
# Time: O(n) → Visit each element exactly once to create nodes
# Space: O(n) → Stack storage for iterative processing
class Solution3:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        # Stack stores (node, left_bound, right_bound) tuples
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        stack = [(root, 0, len(nums) - 1)]
        
        while stack:
            node, left, right = stack.pop()
            
            # Process left subtree
            if left <= node_mid - 1:
                left_mid = left + (node_mid - 1 - left) // 2
                node.left = TreeNode(nums[left_mid])
                stack.append((node.left, left, node_mid - 1))
            
            # Process right subtree  
            if node_mid + 1 <= right:
                right_mid = (node_mid + 1) + (right - (node_mid + 1)) // 2
                node.right = TreeNode(nums[right_mid])
                stack.append((node.right, node_mid + 1, right))
        
        return root

# Alternative Solution 3: Cleaner Iterative Implementation
class Solution3_Alternative:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        # Stack stores (left_index, right_index, parent_node, is_left_child)
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        stack = [(0, mid - 1, root, True), (mid + 1, len(nums) - 1, root, False)]
        
        while stack:
            left, right, parent, is_left = stack.pop()
            
            if left > right:
                continue
                
            mid = left + (right - left) // 2
            node = TreeNode(nums[mid])
            
            if is_left:
                parent.left = node
            else:
                parent.right = node
            
            # Add subtrees to stack
            stack.append((left, mid - 1, node, True))
            stack.append((mid + 1, right, node, False))
        
        return root

# Test function
def test_solutions():
    def inorder_traversal(root):
        """Helper function to verify BST property"""
        if not root:
            return []
        result = []
        result.extend(inorder_traversal(root.left))
        result.append(root.val)
        result.extend(inorder_traversal(root.right))
        return result
    
    def tree_height(root):
        """Helper function to verify balance property"""
        if not root:
            return 0
        return max(tree_height(root.left), tree_height(root.right)) + 1
    
    def is_balanced(root):
        """Check if tree is height-balanced"""
        if not root:
            return True
        
        left_height = tree_height(root.left)
        right_height = tree_height(root.right)
        
        return (abs(left_height - right_height) <= 1 and 
                is_balanced(root.left) and 
                is_balanced(root.right))
    
    # Test case: [1, 3, 5, 7, 9, 11]
    nums = [1, 3, 5, 7, 9, 11]
    
    sol1 = Solution()
    sol2 = Solution2()
    
    tree1 = sol1.sortedArrayToBST(nums)
    tree2 = sol2.sortedArrayToBST(nums)
    
    print(f"Original array: {nums}")
    print(f"BST 1 inorder: {inorder_traversal(tree1)}")  # Should match original
    print(f"BST 2 inorder: {inorder_traversal(tree2)}")  # Should match original
    print(f"BST 1 balanced: {is_balanced(tree1)}")       # Should be True
    print(f"BST 2 balanced: {is_balanced(tree2)}")       # Should be True
    
    # Test edge cases
    empty_tree = sol2.sortedArrayToBST([])
    print(f"Empty array: {empty_tree}")  # Should be None
    
    single_tree = sol2.sortedArrayToBST([5])
    print(f"Single element: {inorder_traversal(single_tree)}")  # Should be [5]

# Interview Strategy:
# 1. Start with Solution 1 (Brute Force) - shows you understand the divide-and-conquer concept
# 2. Optimize to Solution 2 (Index Pointers) - this is what they want to see most
# 3. If time permits, mention Solution 3 (Iterative) as advanced alternative
#
# Key insight: Choose middle element as root to maintain height balance, then recursively build subtrees
# Why Solution 2 is preferred:
# - Optimal O(n) time complexity with no array slicing overhead
# - Clean recursive divide-and-conquer approach
# - Maintains height balance by always choosing middle element
# - Easy to explain and implement under pressure
# - Demonstrates understanding of both BST properties and tree balancing
