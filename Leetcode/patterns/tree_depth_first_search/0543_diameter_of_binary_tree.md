# Leetcode 0543 - Diameter of Binary Tree

## ☀️ UMPIRE

**Understand:** Given the root of a binary tree, return the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. The length of a path between two nodes is represented by the number of edges between them.

**Match:** This is a Tree Traversal problem using DFS (Depth-First Search). The key insight is that for any node, the diameter passing through it equals the sum of the maximum depths of its left and right subtrees. We need to check all nodes and find the maximum diameter.

**Plan:**
1. For each node, calculate the diameter passing through it (left_depth + right_depth)
2. Keep track of the maximum diameter seen so far
3. Use DFS to traverse all nodes and calculate depths
4. Return the maximum diameter found

**Implement:** See the code section below.

**Review:**
- Ensure we visit every node to check all possible diameters
- Verify that we correctly calculate depth and diameter
- Handle edge cases like empty tree and single node

**Evaluate:**
- Time: O(n) for optimal solution - visit each node once
- Space: O(h) where h is height - recursion stack depth

## ☀️ Why This Is a Tree DFS Problem

The diameter can pass through any node in the tree, so we need to:
- **Check every node as a potential "bridge" for the longest path**
- **Calculate the depth of subtrees efficiently**
- **Combine depth calculations with diameter tracking**

Key insights:
- Brute force calculates depth for each node separately (inefficient)
- Optimal solution calculates depth and diameter in single DFS traversal
- For each node: diameter = left_subtree_depth + right_subtree_depth
- We track the global maximum diameter while computing depths bottom-up

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `root = [1,2,3,4,5]` | Standard tree | `3` |
| `root = [1,2]` | Two nodes | `1` |
| `root = [1]` | Single node | `0` |
| `root = []` | Empty tree | `0` |
| `root = [1,2,3,4,5,null,null,6,7]` | Deep left subtree | `4` |

These test:
- Standard balanced and unbalanced trees
- Minimal input sizes
- Empty tree case
- Diameter not passing through root
- Linear tree structures

## ☀️ Code

### Solution 1: Brute Force - Calculate Height for Each Node (暴力解法)
**Time: O(n²) → For each node O(n), calculate height O(n)**  
**Space: O(n) → Recursion stack for both traversal and height calculation**

```python
# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def get_height(node):
            """Calculate height of tree rooted at node"""
            if not node:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1
        
        def get_max_diameter(node):
            """Get maximum diameter in tree rooted at node"""
            if not node:
                return 0
            
            # Diameter passing through current node
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            diameter_through_node = left_height + right_height
            
            # Maximum diameter in left and right subtrees
            left_diameter = get_max_diameter(node.left)
            right_diameter = get_max_diameter(node.right)
            
            return max(diameter_through_node, left_diameter, right_diameter)
        
        return get_max_diameter(root)
```

### Solution 2: Optimized DFS - Single Pass with Global Variable (標準解法)
**Time: O(n) → Visit each node exactly once**  
**Space: O(h) → Recursion stack depth equals tree height**

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def dfs(node):
            """Returns height of subtree, updates global max_diameter"""
            if not node:
                return 0
            
            # Get height of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # Update global maximum diameter
            # Diameter through current node = left_height + right_height
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # Return height of current subtree
            return max(left_height, right_height) + 1
        
        dfs(root)
        return self.max_diameter
```

### Solution 3: Advanced - No Global Variable with Tuple Return (進階解法)
**Time: O(n) → Visit each node exactly once**  
**Space: O(h) → Recursion stack depth equals tree height**

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            """Returns (height, max_diameter_in_subtree)"""
            if not node:
                return 0, 0
            
            left_height, left_max_diameter = dfs(node.left)
            right_height, right_max_diameter = dfs(node.right)
            
            current_height = max(left_height, right_height) + 1
            current_diameter = left_height + right_height
            max_diameter = max(current_diameter, left_max_diameter, right_max_diameter)
            
            return current_height, max_diameter
        
        return dfs(root)[1]
```

## ☀️ Notes

**Key Algorithm Components:**
- `diameter = left_depth + right_depth` for any node
- DFS traversal ensures we check all possible diameters
- Bottom-up approach: calculate depths from leaves to root
- Global tracking: maintain maximum diameter seen across all nodes

**Critical Insight:**
The optimal solution combines depth calculation with diameter tracking in a single traversal. As we return depth information up the tree, we simultaneously check if the current node creates a longer diameter than previously seen.

## ☀️ Coding Walkthrough Script

I'll solve this using DFS to find the diameter efficiently.
The key insight is that the diameter passing through any node equals the sum of the maximum depths of its left and right subtrees.
I'll use a global variable to track the maximum diameter seen so far.
My DFS function will do two things: return the height of the current subtree and update the global maximum diameter.
For each node, I recursively get the heights of left and right subtrees. The diameter through this node is simply left_height + right_height. I update my global maximum if this diameter is larger.
Then I return the height of the current subtree, which is max(left_height, right_height) + 1.
This approach visits each node exactly once, making it O(n) time complexity, which is optimal since we need to examine every node to find the maximum diameter."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Brute Force | O(n²) | O(n) | Calculate height for each node | Simple but inefficient |
| DFS with Global Variable | O(n) | O(h) | Single pass traversal | **Recommended**; clean and optimal |
| DFS with Tuple Return | O(n) | O(h) | No global variable | More functional style |

## ☀️ Tree Diameter Insights

- **Core concept:** Diameter through node = left_subtree_depth + right_subtree_depth
- **Optimization:** Combine depth calculation with diameter tracking
- **Traversal choice:** DFS is natural for tree depth calculations
- **Global vs local:** Global variable simplifies the logic significantly
- **Bottom-up:** Calculate from leaves upward for efficiency

**Mathematical Guarantee:** Since we check every node as a potential bridge for the longest path and the diameter is simply the sum of depths on both sides, examining all nodes ensures we find the global maximum.

**Note:** Solution 2 is the most recommended approach for interviews due to its clarity and optimal performance. Solution 1 shows understanding but is inefficient. Solution 3 demonstrates advanced functional programming concepts but may be harder to explain under time pressure.
