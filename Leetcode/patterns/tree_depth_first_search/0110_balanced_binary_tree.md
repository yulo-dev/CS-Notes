# Leetcode 0110 - Balanced Binary Tree

## ☀️ UMPIRE

**Understand:** Given a binary tree, determine if it is height-balanced. For this problem, a height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

**Match:** This is a Tree Traversal problem using DFS (Depth-First Search) with height calculation. The key insight is that we need to check the balance condition for every node while efficiently calculating subtree heights. This combines tree height calculation with conditional checking.

**Plan:**
1. For each node, calculate heights of left and right subtrees
2. Check if the height difference is at most 1
3. Recursively verify that both subtrees are also balanced
4. Optimize by combining height calculation with balance checking in single traversal

**Implement:** See the code section below.

**Review:**
- Ensure we check balance condition for every node, not just root
- Verify that we handle empty trees and single nodes correctly
- Confirm that we're calculating heights accurately
- Check that early termination works when imbalance is detected

**Evaluate:**
- Time: O(n) for optimal solution - visit each node once
- Space: O(h) where h is tree height - recursion stack depth

## ☀️ Why This Is a Tree DFS Problem

Balance checking requires examining every node's local property while considering global tree structure:
- **Every node must satisfy the balance condition independently**
- **Height calculation naturally uses DFS traversal pattern**
- **We can optimize by combining height and balance checking**
- **Early termination prevents unnecessary computation**

Key insights:
- Brute force calculates height repeatedly for same subtrees (inefficient)
- Optimal solution calculates height once while checking balance
- DFS post-order traversal allows bottom-up height calculation
- Using sentinel values (-1) enables early termination for efficiency

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `root = [3,9,20,null,null,15,7]` | Balanced tree | `true` |
| `root = [1,2,2,3,3,null,null,4,4]` | Unbalanced tree | `false` |
| `root = []` | Empty tree | `true` |
| `root = [1]` | Single node | `true` |
| `root = [1,null,2,null,3]` | Right-skewed tree | `false` |
| `root = [1,2,null,3]` | Left-heavy subtree | `true` |

These test:
- Standard balanced and unbalanced scenarios
- Empty tree boundary condition
- Single node edge case
- Linear tree structures (completely unbalanced)
- Subtle balance cases where height difference is exactly 1

## ☀️ Code

### Solution 1: Brute Force - Separate Height and Balance Check (Brute Force)
**Time: O(n²) → For each node O(n), calculate height O(n)**  
**Space: O(n) → Recursion stack for both traversal and height calculation**

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node):
            """Calculate height of tree rooted at node"""
            if not node:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1
        
        def check_balanced(node):
            """Check if tree rooted at node is balanced"""
            if not node:
                return True
            
            # Calculate heights of left and right subtrees
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            # Check if current node is balanced
            if abs(left_height - right_height) > 1:
                return False
            
            # Recursively check if left and right subtrees are balanced
            return check_balanced(node.left) and check_balanced(node.right)
        
        return check_balanced(root)
```

### Solution 2: Optimized DFS with Early Termination (Classic Solution)
**Time: O(n) → Visit each node exactly once**  
**Space: O(h) → Recursion stack depth equals tree height**

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            """Returns height if balanced, -1 if not balanced"""
            # Base case: empty node is balanced with height 0
            if not node:
                return 0
            
            # Get height of left subtree
            left_height = dfs(node.left)
            if left_height == -1:  # Left subtree is not balanced
                return -1
            
            # Get height of right subtree
            right_height = dfs(node.right)
            if right_height == -1:  # Right subtree is not balanced
                return -1
            
            # Check if current node is balanced
            if abs(left_height - right_height) > 1:
                return -1
            
            # Return height of current subtree
            return max(left_height, right_height) + 1
        
        return dfs(root) != -1
```

### Solution 3: Tuple Return for Clean Separation (Advanced Solution)
**Time: O(n) → Visit each node exactly once**  
**Space: O(h) → Recursion stack depth equals tree height**

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            """Returns (is_balanced, height)"""
            # Base case: empty node is balanced with height 0
            if not node:
                return True, 0
            
            # Check left subtree
            left_balanced, left_height = dfs(node.left)
            if not left_balanced:
                return False, 0
            
            # Check right subtree
            right_balanced, right_height = dfs(node.right)
            if not right_balanced:
                return False, 0
            
            # Check if current node is balanced
            is_balanced = abs(left_height - right_height) <= 1
            height = max(left_height, right_height) + 1
            
            return is_balanced, height
        
        return dfs(root)[0]
```

## ☀️ Notes

**Key Algorithm Components:**
- Height calculation using post-order DFS traversal
- Balance condition check: |left_height - right_height| ≤ 1
- Early termination using sentinel values (-1) to avoid unnecessary computation
- Bottom-up approach: check children before parents

**Critical Insight:**
The optimal solution combines height calculation with balance checking in a single traversal. By using -1 as a sentinel value to indicate imbalance, we can propagate the "not balanced" state up the tree immediately, avoiding redundant calculations.

## ☀️ Coding Walkthrough Script

I'll solve this using an optimized DFS approach that combines height calculation with balance checking.
The key insight is that we need to check the balance condition for every node in the tree, not just the root. A tree is balanced only if every node's left and right subtrees differ in height by at most 1.
My DFS function will return the height of the subtree if it's balanced, or -1 if it's not balanced. This allows for early termination - as soon as we find any unbalanced subtree, we can immediately return -1 and propagate this result up.
For each node, I first recursively check the left subtree. If it returns -1, I know the tree is unbalanced and return -1 immediately. I do the same for the right subtree.
If both subtrees are balanced, I check if the current node maintains the balance condition by comparing the height difference. If the difference is greater than 1, I return -1. Otherwise, I return the height of the current subtree.
This approach visits each node exactly once, making it O(n) time complexity, and uses O(h) space for the recursion stack.

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Brute Force | O(n²) | O(n) | Separate height and balance checks | Simple but inefficient |
| Optimized DFS | O(n) | O(h) | Combined calculation with early termination | **Recommended**; optimal performance |
| Tuple Return | O(n) | O(h) | Clean separation of concerns | More readable but slightly more complex |

## ☀️ Tree Balance Insights

- **Balance definition:** For every node, |height(left) - height(right)| ≤ 1
- **Global property:** All nodes must satisfy balance condition, not just root
- **Optimization key:** Combine height calculation with balance checking
- **Early termination:** Use sentinel values to avoid unnecessary computation
- **Traversal pattern:** Post-order DFS for bottom-up height calculation

**Mathematical Guarantee:** Since we check the balance condition at every node and use accurate height calculations, we can definitively determine if the entire tree satisfies the balanced property.

**Note:** Solution 2 (Optimized DFS) is the most recommended approach for interviews due to its optimal O(n) time complexity, clean implementation, and elegant use of sentinel values for early termination. Solution 1 demonstrates understanding but is inefficient. Solution 3 offers cleaner code structure but may be harder to explain under time pressure.
