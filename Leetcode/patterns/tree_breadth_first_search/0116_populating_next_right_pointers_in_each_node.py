# LeetCode 116: Populating Next Right Pointers in Each Node
# Given a perfect binary tree, populate each next pointer to point to its next right node

from typing import Optional
from collections import deque

# Definition for a Node
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# Time: O(n) → Visit each node once in level order traversal
# Space: O(w) → O(n) worst case, where w is max width of tree level
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # BFS level-by-level approach - use prev pointer to connect nodes
        if not root:
            return root

        queue = deque([root])

        while queue:
            prev = None  # Track previous node in current level

            for i in range(len(queue)):
                node = queue.popleft()

                # Connect previous node to current node
                if prev:
                    prev.next = node

                prev = node  # Update previous node

                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Last node in level points to None (usually default)
            prev.next = None

        return root

# Time: O(n) → Visit each node once using level-by-level iteration
# Space: O(1) → Only use pointers, no additional data structures
# ★ This is the classic solution ★
class Solution2:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        # Optimized approach using existing next pointers - perfect binary tree property
        if not root:
            return None
        
        # Start from the leftmost node of each level
        leftmost = root
        
        while leftmost.left:  # While there are more levels
            # Traverse current level using next pointers
            head = leftmost
            
            while head:
                # Connect children of current node
                head.left.next = head.right
                
                # Connect right child to next node's left child (if exists)
                if head.next:
                    head.right.next = head.next.left
                
                # Move to next node in current level
                head = head.next
            
            # Move to next level
            leftmost = leftmost.left
        
        return root

# Time: O(n) → Visit each node once in recursive calls
# Space: O(h) → where h is the height; for a perfect binary tree h = O(log n)
class Solution3:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        # Recursive DFS approach - connect children during traversal
        if not root or not root.left:
            return root
        
        # Connect direct children
        root.left.next = root.right
        
        # Connect across subtrees if parent has next pointer
        if root.next:
            root.right.next = root.next.left
        
        # Recursively connect subtrees
        self.connect(root.left)
        self.connect(root.right)
        
        return root

# Test function
def test_solutions():
    # Helper function to create perfect binary tree: [1,2,3,4,5,6,7]
    def create_perfect_tree():
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        return root
    
    # Helper function to print next pointers
    def print_next_pointers(root):
        if not root:
            return "None"
        
        result = []
        leftmost = root
        
        while leftmost:
            current = leftmost
            level = []
            while current:
                level.append(str(current.val))
                current = current.next
            result.append("->".join(level) + "->None")
            leftmost = leftmost.left
        
        return result
    
    # Test Solution 1 (BFS)
    tree1 = create_perfect_tree()
    sol1 = Solution()
    result1 = sol1.connect(tree1)
    print("BFS Solution:")
    print(print_next_pointers(result1))
    
    # Test Solution 2 (Optimized)
    tree2 = create_perfect_tree()
    sol2 = Solution2()
    result2 = sol2.connect(tree2)
    print("\nOptimized Solution:")
    print(print_next_pointers(result2))
    
    # Test Solution 3 (Recursive)
    tree3 = create_perfect_tree()
    sol3 = Solution3()
    result3 = sol3.connect(tree3)
    print("\nRecursive Solution:")
    print(print_next_pointers(result3))
    
    # Test edge cases
    print("\nEdge Cases:")
    print(f"Empty tree - BFS: {sol1.connect(None)}")
    
    single = Node(1)
    print(f"Single node - Optimized: {sol2.connect(single).val if sol2.connect(single) else None}")


# 1. Start with Solution 1 (BFS) 
# 2. Optimize to Solution 2 (O(1) space) 
# 3. If time permits, mention Solution 3 (Recursive) - demonstrates DFS thinking
#
# Key insight: Perfect binary tree allows O(1) space solution using existing next pointers
# Solution 2 is preferred: Optimal space complexity, leverages problem constraints
