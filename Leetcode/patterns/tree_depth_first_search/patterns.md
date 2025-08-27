# Tree DFS — Patterns Summary

This guide consolidates common **Tree DFS** patterns you'll see across LeetCode. 
It teaches you **when to use which pattern**, **how to recognize** the right approach, core **tips/pitfalls**, a short **template**, and **example problems** you've solved.

---

## Pattern 1 — Tree Validation (Property Checking)

### When to Use
- Verify if a tree satisfies certain **structural or value properties**.
- Check global constraints that must hold for all nodes.

### How to Recognize
- Keywords: "valid", "balanced", "BST", "validate"
- Need to verify tree-wide properties, not just local relationships
- Often requires range/constraint propagation through recursion

### Tips / Pitfalls
- **Global vs Local**: Tree properties often require global checking, not just parent-child relationships
- Use **range bounds** for BST validation instead of just comparing with parent
- **Height difference** for balance checking requires bottom-up information

### Template
```python
def validateTree(root):
    def dfs(node, min_bound, max_bound):
        if not node:
            return True
        
        # Check current node constraint
        if not (min_bound < node.val < max_bound):
            return False
            
        # Propagate updated constraints to children
        return (dfs(node.left, min_bound, node.val) and 
                dfs(node.right, node.val, max_bound))
    
    return dfs(root, float('-inf'), float('inf'))
```

### Problems
- **0098 – Validate Binary Search Tree**
- **0110 – Balanced Binary Tree**

---

## Pattern 2 — Tree Measurement (Height/Depth/Distance)

### When to Use
- Calculate **quantitative properties** like height, depth, diameter, or distances.
- Often involves **bottom-up information aggregation**.

### How to Recognize
- Keywords: "height", "depth", "diameter", "maximum", "distance"
- Need to combine information from subtrees
- Return numeric values representing tree measurements

### Tips / Pitfalls
- **Bottom-up approach**: Calculate child measurements first, then parent
- **Global variable** or **return tuple** to track both local and global information
- **Diameter calculation**: `left_depth + right_depth` at each node

### Template
```python
def measureTree(root):
    self.global_result = 0
    
    def dfs(node):
        if not node:
            return 0
            
        left_measurement = dfs(node.left)
        right_measurement = dfs(node.right)
        
        # Update global result if needed
        current_measurement = left_measurement + right_measurement
        self.global_result = max(self.global_result, current_measurement)
        
        # Return measurement for parent
        return max(left_measurement, right_measurement) + 1
    
    dfs(root)
    return self.global_result
```

### Problems
- **0104 – Maximum Depth of Binary Tree**
- **0543 – Diameter of Binary Tree**

---

## Pattern 3 — Tree View/Traversal (Perspective-Based)

### When to Use
- Extract nodes visible from certain **perspectives or orders**.
- **Level-aware** or **position-aware** traversal.

### How to Recognize
- Keywords: "right side view", "level order", "inorder", "preorder"
- Need to collect nodes based on their position or visibility
- Often requires **level tracking** or **order-specific** processing

### Tips / Pitfalls
- **BFS vs DFS trade-off**: BFS natural for levels, DFS better for space in some cases
- **Right-first traversal**: For right side view, process right before left
- **Early termination**: Stop when you have enough information

### Template
```python
def treeView(root):
    result = []
    
    def dfs(node, level):
        if not node:
            return
            
        # First time visiting this level
        if level == len(result):
            result.append(node.val)
        
        # Order matters: right first for right view
        dfs(node.right, level + 1)
        dfs(node.left, level + 1)
    
    dfs(root, 0)
    return result
```

### Problems
- **0199 – Binary Tree Right Side View**

---

## Pattern 4 — Tree Transformation (Structure Modification)

### When to Use
- **Modify tree structure** while maintaining certain properties.
- **Reverse operations**: Build from array or flatten to list.

### How to Recognize
- Keywords: "convert", "flatten", "invert", "build", "construct"
- Input/output involves different tree structures or formats
- Need to create new structure or modify existing one

### Tips / Pitfalls
- **Reverse thinking**: Sometimes building backwards is more elegant
- **Divide and conquer**: Split problem into smaller identical subproblems
- **Index arithmetic**: For array-to-tree conversion, careful with mid calculation

### Template
```python
def transformTree(root):
    def dfs(node):
        if not node:
            return None
            
        # Transform children first (post-order for some cases)
        left = dfs(node.left)
        right = dfs(node.right)
        
        # Apply transformation to current node
        # This varies greatly by specific transformation
        node.left = right  # Example: swap children
        node.right = left
        
        return node
    
    return dfs(root)
```

### Problems
- **0108 – Convert Sorted Array to Binary Search Tree**
- **0114 – Flatten Binary Tree to Linked List**
- **0226 – Invert Binary Tree**

---

## Pattern 5 — BST Operations (Search Tree Properties)

### When to Use
- Leverage **BST ordering properties** for efficient operations.
- **O(h) complexity** instead of O(n) by using structure.

### How to Recognize
- Input is specifically a **Binary Search Tree**
- Keywords: "BST", "inorder", "successor", "search"
- Can eliminate subtrees based on value comparisons

### Tips / Pitfalls
- **Inorder gives sorted sequence**: Use for k-th element problems
- **Iterative often better**: BST paths are predictable, avoid recursion overhead
- **Three-way decision**: both left, both right, or split point

### Template
```python
def bstOperation(root, target):
    current = root
    
    while current:
        if condition_left(current, target):
            current = current.left
        elif condition_right(current, target):
            current = current.right
        else:
            return current  # Found answer
    
    return None
```

### Problems
- **0230 – Kth Smallest Element in a BST**
- **0235 – Lowest Common Ancestor of a Binary Search Tree**
- **0285 – Inorder Successor in BST**

---

## Pattern 6 — Tree Ancestry/Relationship (Node Relations)

### When to Use
- Find **relationships between nodes**: ancestors, descendants, LCA.
- **Path-based reasoning** or **subtree membership**.

### How to Recognize
- Keywords: "lowest common ancestor", "path", "parent", "ancestor"
- Need to understand node relationships across different subtrees
- Often involves **bottom-up information propagation**

### Tips / Pitfalls
- **Bottom-up approach**: Process children before making decisions about parent
- **Return meaningful values**: Use return values to communicate findings upward
- **BST vs Generic tree**: BST allows value-based elimination

### Template
```python
def findRelationship(root, p, q):
    def dfs(node):
        if not node:
            return None
            
        # Process children first
        left_result = dfs(node.left)
        right_result = dfs(node.right)
        
        # Make decision based on current node and children results
        if condition_met(node, left_result, right_result):
            return node
            
        # Propagate result upward
        return left_result or right_result
    
    return dfs(root)
```

### Problems
- **0235 – Lowest Common Ancestor of a Binary Search Tree**
- **0236 – Lowest Common Ancestor of a Binary Tree**

---

## Pattern 7 — Tree Deletion/Pruning (Selective Removal)

### When to Use
- **Remove nodes** based on certain criteria while maintaining tree integrity.
- **Forest creation** after deletions.

### How to Recognize
- Keywords: "delete", "remove", "prune", "forest"
- Need to disconnect nodes and handle resulting subtrees
- Children of deleted nodes often become new roots

### Tips / Pitfalls
- **Post-order processing**: Handle children before deciding parent's fate
- **Return None for deletion**: Use return value to disconnect nodes
- **Root status propagation**: When parent deleted, children become roots

### Template
```python
def deleteNodes(root, to_delete):
    delete_set = set(to_delete)
    result = []
    
    def dfs(node, is_root):
        if not node:
            return None
            
        deleted = node.val in delete_set
        
        # Process children (they become roots if current deleted)
        node.left = dfs(node.left, deleted)
        node.right = dfs(node.right, deleted)
        
        # Handle current node
        if deleted:
            return None  # Disconnect
        if is_root:
            result.append(node)  # Add to forest
        return node
    
    dfs(root, True)
    return result
```

### Problems
- **1110 – Delete Nodes and Return Forest**

---

## Quick Recognition Guide

- **"Validate" / "Check if valid"** → Pattern 1 (Tree Validation)
- **"Height" / "Depth" / "Diameter" / "Maximum"** → Pattern 2 (Tree Measurement)
- **"View" / "Traversal" / "Order" / "Level"** → Pattern 3 (Tree View/Traversal)
- **"Convert" / "Build" / "Flatten" / "Invert"** → Pattern 4 (Tree Transformation)
- **"BST" / "Inorder" / "Kth element" / "Successor"** → Pattern 5 (BST Operations)
- **"Lowest Common Ancestor" / "Path" / "Parent"** → Pattern 6 (Tree Ancestry/Relationship)
- **"Delete" / "Remove" / "Forest" / "Prune"** → Pattern 7 (Tree Deletion/Pruning)

---

## General Tips

- **Choose traversal order wisely**: Pre-order for top-down, post-order for bottom-up, in-order for BST
- **Return value strategy**: Use return values to pass information upward in recursion
- **State management**: Use parameters for top-down info, return values for bottom-up info
- **BST optimization**: Leverage ordering properties to reduce time complexity
- **Space complexity**: Consider iterative solutions for space-critical scenarios

---

## Problems Mapped by Pattern

**Pattern 1 (Validation)**: 0098, 0110  
**Pattern 2 (Measurement)**: 0104, 0543  
**Pattern 3 (View/Traversal)**: 0199  
**Pattern 4 (Transformation)**: 0108, 0114, 0226  
**Pattern 5 (BST Operations)**: 0230, 0235, 0285  
**Pattern 6 (Ancestry/Relationship)**: 0235, 0236  
**Pattern 7 (Deletion/Pruning)**: 1110  

---
