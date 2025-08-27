# Leetcode 1110 - Delete Nodes and Return Forest

## ☀️ UMPIRE

**Understand:** Given the root of a binary tree, each node in the tree has a distinct value. After deleting all nodes with values in to_delete, we are left with a forest (a disjoint union of trees). Return the roots of the trees in the remaining forest.

**Match:** This is a Tree Modification problem using DFS (Depth-First Search) with post-order traversal. The key insight is that when a node is deleted, its children (if they exist and are not deleted) become new roots in the forest. We need to process children before deciding the fate of the current node.

**Plan:**
1. Use DFS with post-order traversal (process children first)
2. For each node, recursively process left and right children
3. If a node is to be deleted, its children become potential roots
4. If current node is not deleted and is a root, add it to the result forest
5. Return None for deleted nodes to disconnect them from their parents

**Implement:** See the code section below.

**Review:**
- Ensure we process children before current node (post-order)
- Verify that deleted nodes are properly disconnected (return None)
- Check that orphaned children are correctly identified as new roots
- Confirm we handle edge cases like deleting the root or all nodes

**Evaluate:**
- Time: O(n) - visit each node exactly once
- Space: O(h + k) where h is tree height, k is size of to_delete set

## ☀️ Why This Is a Tree DFS Post-Order Problem

Tree deletion with forest creation requires post-order processing:
- **Children must be processed before parent** to handle cascading effects
- **Parent deletion creates new roots from children** requiring bottom-up approach
- **Single traversal efficiency** by combining deletion and root identification
- **Natural disconnection** by returning None for deleted nodes

Key insights:
- Pre-order would require complex parent tracking and multiple passes
- Post-order naturally handles the "children become roots when parent deleted" logic
- In-line computation of child root status eliminates need for separate state variables
- Set lookup provides O(1) deletion checking for efficiency

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `root = [1,2,3,4,5,6,7], to_delete = [3,5]` | Standard deletion case | `[[1,2,4], [6], [7]]` |
| `root = [1,2,4,null,3], to_delete = [3]` | Leaf node deletion | `[[1,2,4]]` |
| `root = [1], to_delete = [1]` | Delete entire tree | `[]` |
| `root = [1,2,3], to_delete = []` | No deletions | `[[1,2,3]]` |
| `root = [1,2,3,4,5,6,7], to_delete = [1]` | Delete root only | `[[2,4,5], [3,6,7]]` |

These test:
- Standard multi-node deletion scenarios
- Leaf node deletion (no new roots created)
- Complete tree deletion (empty forest)
- No deletion case (original tree returned)
- Root deletion (children become new forest roots)

## ☀️ Code

### Solution 1: Brute Force - Multiple Tree Passes (Brute Force)
**Time: O(n * k) → k passes over tree, each pass O(n) where k = len(to_delete)**  
**Space: O(n) → Store intermediate tree structures and recursion stack**

```python
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
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
            
            # Search and delete in subtrees with complex parent management
            new_roots = []
            # ... complex deletion logic for each subtree
            return new_roots
        
        # Multiple passes, one for each deletion target
        current_roots = [root]
        for target in to_delete:
            next_roots = []
            for tree_root in current_roots:
                # Process each tree separately
                pass
            current_roots = next_roots
        
        return current_roots
```

### Solution 2: Single-Pass DFS with Elegant Post-Order (Classic Solution)
**Time: O(n) → Visit each node exactly once**  
**Space: O(h + k) → Recursion stack depth + set storage for to_delete values**

```python
class Solution:
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
```

### Solution 3: Post-Order with Explicit Parent Tracking (Advanced Solution)
**Time: O(n) → Visit each node exactly once**  
**Space: O(h + k) → Recursion stack depth + set storage**

```python
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        result = []
        
        def postorder(node, parent, is_left_child):
            """Post-order traversal with explicit parent tracking"""
            if not node:
                return
            
            # Process children first (post-order)
            postorder(node.left, node, True)
            postorder(node.right, node, False)
            
            # Process current node after children are handled
            if node.val in to_delete_set:
                # Current node will be deleted - disconnect and promote children
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
```

## ☀️ Notes

**Key Algorithm Components:**
- Post-order DFS traversal for proper deletion sequencing
- Set-based O(1) lookup for deletion candidates
- In-line root status computation for children nodes
- Elegant None return for node disconnection

**Critical Insight:**
The brilliance of Solution 2 lies in its elegant post-order approach where children are processed first, allowing natural handling of the "orphaned children become roots" scenario. The in-line computation of `node.val in dels` for determining child root status eliminates the need for complex state management.

## ☀️ Coding Walkthrough Script

"I'll solve this using a single-pass DFS with post-order traversal that elegantly handles both deletion and forest creation.

The key insight is that when a node is deleted, its children automatically become new roots in the forest. This suggests a post-order approach where I process children before making decisions about the current node.

I use a helper function that takes a node and a boolean indicating whether it's currently a root. For each node, I first recursively process both children, passing them a root status based on whether the current node will be deleted.

The magic happens in this line: `node.left = dfs(node.left, node.val in dels)`. If the current node is in the deletion set, its children become roots. Otherwise, they remain regular children.

After processing children, I check if the current node should be deleted. If so, I return None to disconnect it from its parent - this automatically promotes the children I just processed.

If the node survives deletion and is marked as a root, I add it to the forest.

This approach is elegant because it combines deletion, disconnection, and root identification in a single traversal. The post-order nature ensures that by the time I process any node, all its descendants have already been properly handled.

The time complexity is O(n) since I visit each node once, and space complexity is O(h + k) for the recursion stack plus the deletion set."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Multiple Passes | O(n * k) | O(n) | Process each deletion separately | Simple but inefficient |
| Single-Pass DFS | O(n) | O(h + k) | Post-order with elegant state management | **Recommended**; optimal and clean |
| Explicit Parent Tracking | O(n) | O(h + k) | Manual parent-child relationship management | More complex implementation |

## ☀️ Tree Forest Creation Insights

- **Post-order advantage:** Children processed before parent decisions
- **Elegant state passing:** Root status computed in-line during recursion
- **Natural disconnection:** None return value handles parent-child unlinking
- **Single-pass efficiency:** Combine deletion detection, node removal, and root identification
- **Set optimization:** O(1) deletion lookup instead of O(k) list search
**Note:** Solution 2 is the most recommended approach for interviews due to its optimal O(n) time complexity, elegant post-order logic, and clean integration of deletion and forest creation. The in-line computation of child root status and natural disconnection through None returns make this solution both efficient and beautiful. This approach demonstrates advanced understanding of tree traversal patterns and state management.
