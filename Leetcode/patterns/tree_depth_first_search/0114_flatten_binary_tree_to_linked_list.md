# Leetcode 0114 - Flatten Binary Tree to Linked List

## ☀️ UMPIRE

**Understand:** Given the root of a binary tree, flatten the tree into a "linked list" where the right child pointer points to the next node in the list and the left child pointer is always null. The "linked list" should be in the same order as a pre-order traversal of the binary tree.

**Match:** This is a Tree Modification problem using DFS (Depth-First Search) with clever traversal ordering. The key insight is that instead of building the result in pre-order, we can use reverse post-order traversal (right → left → root) to naturally construct the flattened structure backwards.

**Plan:**
1. Use reverse post-order traversal: process right subtree, then left subtree, then current node
2. Maintain a pointer to the previously processed node
3. For each node, set its right pointer to the previous node and clear its left pointer
4. Update the previous pointer to current node

**Implement:** See the code section below.

**Review:**
- Ensure we traverse in correct reverse post-order sequence
- Verify that left pointers are properly cleared to null
- Check that right pointers correctly form the linked list
- Confirm that the final result follows pre-order sequence

**Evaluate:**
- Time: O(n) - visit each node exactly once
- Space: O(h) where h is tree height - recursion stack depth

## ☀️ Why This Is a Reverse Traversal Problem

The flattening requires pre-order sequence but building backwards is more elegant:
- **Pre-order traversal gives us the desired final sequence** (root → left → right)
- **Reverse post-order traversal visits nodes in reverse of that sequence**
- **Building backwards eliminates complex subtree connection logic**
- **Each node naturally points to the previously processed node**

Key insights:
- Forward construction requires complex tracking of subtree tails and connections
- Reverse construction lets each node simply point to the previous node
- The traversal order (right → left → root) is exactly the reverse of pre-order
- This approach transforms a complex connection problem into a simple linking problem

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `root = [1,2,5,3,4,null,6]` | Standard tree | `[1,null,2,null,3,null,4,null,5,null,6]` |
| `root = []` | Empty tree | `[]` |
| `root = [0]` | Single node | `[0]` |
| `root = [1,2,null,3]` | Left-heavy tree | `[1,null,2,null,3]` |
| `root = [1,null,2,null,3]` | Already right-skewed | `[1,null,2,null,3]` |

These test:
- Standard binary tree flattening
- Empty tree boundary condition  
- Single node edge case
- Trees with missing subtrees
- Already flattened trees

## ☀️ Code

### Solution 1: Brute Force - Store and Rebuild (Brute Force)
**Time: O(n) → Visit each node twice (traverse + rebuild)**  
**Space: O(n) → Store all node values in list**

```python
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        # Step 1: Get preorder traversal values
        def preorder(node):
            if not node:
                return []
            result = [node.val]
            result.extend(preorder(node.left))
            result.extend(preorder(node.right))
            return result
        
        values = preorder(root)
        
        # Step 2: Rebuild tree as right-skewed linked list
        current = root
        for i in range(1, len(values)):
            current.left = None
            current.right = TreeNode(values[i])
            current = current.right
```

### Solution 2: Reverse Post-Order Traversal (Classic Solution)
**Time: O(n) → Visit each node exactly once**  
**Space: O(h) → Recursion stack depth equals tree height**

```python
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.prev = None

        def dfs(node):
            if not node:
                return

            # Traverse in reverse preorder: right -> left -> root
            dfs(node.right)
            dfs(node.left)

            # Process current node: link it to previously processed node
            node.right = self.prev
            node.left = None
            self.prev = node

        dfs(root)
```

### Solution 3: Morris-like Iterative Approach (Advanced Solution)
**Time: O(n) → Visit each node with constant operations**  
**Space: O(1) → No recursion, only constant extra space**

```python
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        current = root
        
        while current:
            # If current node has left child
            if current.left:
                # Find the rightmost node in left subtree
                predecessor = current.left
                while predecessor.right:
                    predecessor = predecessor.right
                
                # Connect rightmost node of left subtree to original right subtree
                predecessor.right = current.right
                
                # Move left subtree to right and clear left
                current.right = current.left
                current.left = None
            
            # Move to next node in the flattened structure
            current = current.right
```

## ☀️ Notes

**Key Algorithm Components:**
- Reverse post-order traversal: right → left → root
- Previous node tracking to build linked connections
- Left pointer clearing to maintain linked list format
- In-place modification without creating new nodes

**Critical Insight:**
The genius of the reverse post-order approach is that it transforms a complex tree restructuring problem into a simple linked list construction problem. By processing nodes in reverse pre-order sequence, each node can simply point to the previously processed node.

## ☀️ Coding Walkthrough Script

"I'll solve this using a clever reverse traversal approach that builds the flattened structure backwards.

The key insight is that while we want the final result in pre-order sequence (root, left, right), we can build it more elegantly by traversing in reverse post-order (right, left, root).

I maintain a 'prev' pointer that tracks the previously processed node. As I traverse, each node simply points its right pointer to the previous node and clears its left pointer.

The traversal order is crucial: I visit right subtree first, then left subtree, then process the current node. This ensures that when I process any node, all nodes that should come after it in the final sequence have already been processed and linked.

For example, in a tree with nodes 1,2,3,4,5,6 in pre-order, my traversal visits them in reverse order: 6,5,4,3,2,1. As I visit each node, I link it to the chain I've built so far.

This approach is elegant because it avoids the complexity of figuring out how to connect different subtrees - the traversal order naturally gives us the right linking sequence.

The time complexity is O(n) since I visit each node once, and space complexity is O(h) for the recursion stack."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Store and Rebuild | O(n) | O(n) | Extract values, rebuild structure | Simple but memory inefficient |
| Reverse Post-Order | O(n) | O(h) | Build backwards with elegant traversal | **Recommended**; genius approach |
| Morris-like Iterative | O(n) | O(1) | In-place rearrangement | Space-optimal but complex |

## ☀️ Tree Flattening Insights

- **Reverse thinking advantage:** Building backwards can be simpler than forward construction
- **Traversal order matters:** Right → left → root gives reverse pre-order sequence
- **Simple linking:** Each node points to previously processed node
- **In-place efficiency:** No need to create new nodes or store intermediate values
- **Elegant simplification:** Transform complex tree restructuring into simple list building

**Mathematical Guarantee:** Since reverse post-order traversal visits nodes in exactly the reverse sequence of pre-order traversal, building the linked structure backwards while traversing will produce the correct pre-order flattened result.
