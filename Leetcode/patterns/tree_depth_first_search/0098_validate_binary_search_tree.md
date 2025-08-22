# Leetcode 0098 - Validate Binary Search Tree

## ☀️ UMPIRE

**Understand:** Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as: the left subtree of a node contains only nodes with keys less than the node's key, the right subtree contains only nodes with keys greater than the node's key, and both subtrees must also be binary search trees.

**Match:** This is a Tree Traversal problem with constraint validation using DFS (Depth-First Search). The key insight is that BST properties must hold globally, not just locally. We need to track valid ranges for each node to ensure the BST constraint is satisfied throughout the entire tree structure.

**Plan:**
1. Use DFS with range bounds to validate each node
2. For each node, check if its value falls within the valid range
3. Update bounds when recursing: left subtree gets upper bound = current value, right subtree gets lower bound = current value
4. Return false immediately if any constraint is violated

**Implement:** See the code section below.

**Review:**
- Ensure we check global BST constraints, not just parent-child relationships
- Verify that we handle duplicate values correctly (BST doesn't allow duplicates)
- Check edge cases like empty tree, single node, and boundary values
- Confirm that bounds are updated correctly for left and right subtrees

**Evaluate:**
- Time: O(n) - visit each node exactly once
- Space: O(h) where h is tree height - recursion stack depth

## ☀️ Why This Is a Tree DFS with Constraint Problem

BST validation requires checking global constraints that span multiple levels:
- **Local validation is insufficient** (just checking parent-child relationships misses violations)
- **Global constraints require range tracking** through the entire path from root
- **DFS naturally maintains the path context** needed for range validation
- **Each recursive call narrows the valid range** based on BST properties

Key insights:
- A common mistake is only checking immediate parent-child relationships
- BST property must hold for all ancestors, not just immediate parent
- Range bounds propagate down the tree: left subtree inherits upper bound, right subtree inherits lower bound
- DFS with bounds checking catches all violations in a single pass

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `root = [2,1,3]` | Valid simple BST | `true` |
| `root = [5,1,4,null,null,3,6]` | Invalid: 3 < 5 but in right subtree | `false` |
| `root = [1,1]` | Invalid: duplicate values | `false` |
| `root = [10,5,15,null,null,6,20]` | Invalid: 6 < 10 but in right subtree | `false` |
| `root = []` | Empty tree | `true` |
| `root = [1]` | Single node | `true` |

These test:
- Valid and invalid BST structures
- Global constraint violations (not just local)
- Duplicate value handling
- Empty tree and single node edge cases
- Complex cases where violations occur deep in subtrees

## ☀️ Code

### Solution 1: Brute Force - Check Min/Max for Each Subtree (Brute Force)
**Time: O(n²) → For each node, potentially check against all descendants**  
**Space: O(h) → Recursion stack depth equals tree height**

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def get_min_max(node):
            """Get minimum and maximum values in subtree"""
            if not node:
                return float('inf'), float('-inf')
            
            if not node.left and not node.right:
                return node.val, node.val
            
            left_min, left_max = get_min_max(node.left)
            right_min, right_max = get_min_max(node.right)
            
            subtree_min = min(node.val, left_min, right_min)
            subtree_max = max(node.val, left_max, right_max)
            
            return subtree_min, subtree_max
        
        def validate(node):
            """Check if subtree rooted at node is valid BST"""
            if not node:
                return True
            
            if not validate(node.left) or not validate(node.right):
                return False
            
            if node.left:
                _, left_max = get_min_max(node.left)
                if left_max >= node.val:
                    return False
            
            if node.right:
                right_min, _ = get_min_max(node.right)
                if right_min <= node.val:
                    return False
            
            return True
        
        return validate(root)
```

### Solution 2: DFS with Range Bounds (Classic Solution)
**Time: O(n) → Visit each node exactly once**  
**Space: O(h) → Recursion stack depth equals tree height**

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function that checks whether the current node is within a valid range
        def dfs(node, lower, upper):
            # Base case: empty node is valid by default
            if not node:
                return True
            
            # If the current value violates the BST property, return False
            if not (lower < node.val < upper):
                return False
            
            # Recursively validate the left subtree with updated upper bound
            if not dfs(node.left, lower, node.val):
                return False
            
            # Recursively validate the right subtree with updated lower bound
            if not dfs(node.right, node.val, upper):
                return False
            
            # Current node and subtrees are valid
            return True
        
        # Start recursion with the full valid range
        return dfs(root, float('-inf'), float('inf'))
```

### Solution 3: Inorder Traversal with Monotonic Check (Advanced Solution)
**Time: O(n) → Visit each node exactly once**  
**Space: O(h) → Recursion stack depth equals tree height**

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node):
            """Inorder traversal: left -> root -> right"""
            if not node:
                return True
            
            # Traverse left subtree
            if not inorder(node.left):
                return False
            
            # Check current node against previous value
            # In valid BST, inorder traversal gives strictly increasing sequence
            if node.val <= self.prev_val:
                return False
            self.prev_val = node.val
            
            # Traverse right subtree
            return inorder(node.right)
        
        self.prev_val = float('-inf')
        return inorder(root)
```

## ☀️ Notes

**Key Algorithm Components:**
- Range bound tracking to enforce global BST constraints
- Proper bound updates: left subtree inherits upper bound, right subtree inherits lower bound
- Early termination when constraints are violated
- Handling of duplicate values (strict inequality in BST)

**Critical Insight:**
The most common mistake in BST validation is only checking local parent-child relationships. The range bounds approach ensures that every node satisfies the BST property with respect to all its ancestors, not just its immediate parent.

## ☀️ Coding Walkthrough Script

I'll solve this using DFS with range bounds to ensure global BST constraints are satisfied.
The key insight is that for each node, I need to track the valid range of values it can have based on all its ancestors, not just its immediate parent.
My DFS helper function takes three parameters: the current node and the lower and upper bounds for valid values. I start with the full range from negative to positive infinity.
For each node, I first check if its value falls within the valid range. If not, I return false immediately.
Then I recursively validate the left subtree, updating the upper bound to the current node's value since all nodes in the left subtree must be smaller. Similarly, for the right subtree, I update the lower bound since all nodes must be larger.
This approach catches violations like having a value that's smaller than the root but incorrectly placed in the right subtree, which a naive parent-child check would miss.
The time complexity is O(n) since I visit each node once, and space complexity is O(h) for the recursion stack.

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Brute Force Min/Max | O(n²) | O(h) | Check subtree ranges for each node | Simple but inefficient |
| DFS Range Bounds | O(n) | O(h) | Track valid range for each node | **Recommended**; optimal and intuitive |
| Inorder Traversal | O(n) | O(h) | Verify strictly increasing sequence | Elegant property-based approach |

## ☀️ BST Validation Insights

- **Global vs Local:** BST property must hold globally across all ancestor-descendant relationships
- **Range propagation:** Valid range narrows as we traverse down the tree
- **Duplicate handling:** BST typically doesn't allow duplicates (use strict inequalities)
- **Inorder property:** Valid BST produces strictly increasing inorder traversal
- **Common pitfall:** Only checking immediate parent-child relationships misses global violations

**Mathematical Guarantee:** Since we enforce the BST constraint at every node with respect to all its ancestors through range bounds, we can definitively determine if the entire tree satisfies the BST property.

**Note:** Solution 2 (DFS with Range Bounds) is the most recommended approach for interviews due to its optimal performance, intuitive logic, and clear step-by-step validation process. The explicit early returns and range checking make it easy to explain and debug during interviews. The inorder approach (Solution 3) is elegant but may be harder to explain under time pressure.
