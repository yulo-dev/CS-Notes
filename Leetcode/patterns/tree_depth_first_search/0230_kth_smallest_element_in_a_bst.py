# LeetCode 230: Kth Smallest Element in a BST
# Given the root of a binary search tree, and an integer k, 
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

from typing import Optional, List

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1: Brute Force - Inorder Traversal with Full List
# Time: O(n) → Visit all nodes to build complete sorted list
# Space: O(n) → Store all node values in list
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            """Collect all values using inorder traversal"""
            if not node:
                return []
            
            result = []
            result.extend(inorder(node.left))   # Left subtree
            result.append(node.val)             # Current node
            result.extend(inorder(node.right))  # Right subtree
            
            return result
        
        # Get all values in sorted order and return kth element
        sorted_values = inorder(root)
        return sorted_values[k - 1]  # k is 1-indexed

# Solution 2: Optimized Inorder with Early Termination (Classic Solution)
# Time: O(h + k) → Best case O(log n + k), worst case O(n) when k = n
# Space: O(h) → Recursion stack depth equals tree height

class Solution2:
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

# Solution 3: Advanced - Iterative Inorder with Stack
# Time: O(h + k) → Best case O(log n + k), worst case O(n) when k = n
# Space: O(h) → Stack storage for iterative traversal
class Solution3:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """Iterative inorder traversal using stack"""
        stack = []
        current = root
        count = 0
        
        while stack or current:
            # Go to leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Process current node
            current = stack.pop()
            count += 1
            
            # If this is the kth node, return its value
            if count == k:
                return current.val
            
            # Move to right subtree
            current = current.right
        
        return -1  # Should never reach here for valid input

# Alternative Solution 3: Using Generator for Clean Code
class Solution3_Alternative:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_generator(node):
            """Generator that yields values in inorder sequence"""
            if node:
                yield from inorder_generator(node.left)
                yield node.val
                yield from inorder_generator(node.right)
        
        # Get the kth element from the generator
        for i, val in enumerate(inorder_generator(root)):
            if i == k - 1:  # k is 1-indexed
                return val
        
        return -1  # Should never reach here for valid input

# Test function
def test_solutions():
    # Create test BST:      3
    #                      / \
    #                     1   4
    #                      \
    #                       2
    # Inorder: [1, 2, 3, 4]
    # Expected for k=1: 1, k=2: 2, k=3: 3, k=4: 4
    
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    
    sol1 = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    
    for k in [1, 2, 3, 4]:
        result1 = sol1.kthSmallest(root, k)
        
        # Create fresh instance for Solution2 since it uses instance variables
        sol2_fresh = Solution2()
        result2 = sol2_fresh.kthSmallest(root, k)
        
        result3 = sol3.kthSmallest(root, k)
        
        print(f"k={k}: Brute Force={result1}, Optimized={result2}, Iterative={result3}")
    
    # Test larger BST:      5
    #                      / \
    #                     3   6
    #                    / \
    #                   2   4
    #                  /
    #                 1
    # Inorder: [1, 2, 3, 4, 5, 6]
    
    larger_root = TreeNode(5)
    larger_root.left = TreeNode(3)
    larger_root.right = TreeNode(6)
    larger_root.left.left = TreeNode(2)
    larger_root.left.right = TreeNode(4)
    larger_root.left.left.left = TreeNode(1)
    
    print(f"\nLarger BST - k=3: {sol3.kthSmallest(larger_root, 3)}")  # Expected: 3
    print(f"Larger BST - k=5: {sol3.kthSmallest(larger_root, 5)}")    # Expected: 5

# Strategy:
# 1. Start with Solution 1 (Brute Force) - shows you understand BST inorder property
# 2. Optimize to Solution 2 (Early Termination) - this is what they want to see most
# 3. If time permits, mention Solution 3 (Iterative) as space-conscious alternative
#
# Key insight: BST inorder traversal gives sorted sequence, so kth smallest = kth element in inorder
# Solution 2 is preferred:
# - Intuitive countdown approach: start with k, decrement until 0
# - Clean early termination with immediate return
# - Leverages BST property perfectly (inorder = sorted)
# - Easy to explain: "I visit nodes in sorted order and stop at the kth one"
# - Shows understanding of both BST properties and traversal optimization
