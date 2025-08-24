# Leetcode 0285 - Inorder Successor in BST

## ☀️ UMPIRE

**Understand:** Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null. The successor of a node p is the node with the smallest key greater than p.val.

**Match:** This is a BST Search problem that leverages BST ordering properties. The key insight is that the inorder successor is simply the smallest node with value greater than p.val, and BST structure allows us to find this efficiently without traversing the entire tree.

**Plan:**
1. Use BST property: left < root < right
2. Search for the smallest value greater than p.val
3. When current.val > p.val, it's a potential successor, but search left for smaller candidates
4. When current.val <= p.val, successor must be in right subtree
5. Return the best candidate found

**Implement:** See the code section below.

**Review:**
- Ensure we find the smallest value greater than p.val (not just any greater value)
- Verify that we handle cases where no successor exists
- Check that we leverage BST property for optimal time complexity
- Confirm we handle edge cases like p being the maximum value

**Evaluate:**
- Time: O(h) - best case O(log n) for balanced BST, worst case O(n) for skewed
- Space: O(1) - only constant extra space for iterative approach

## ☀️ Why This Is a BST Property Search Problem

BST structure provides the key optimization for finding successors:
- **Inorder traversal of BST produces sorted sequence** - successor is next in this sequence
- **BST ordering eliminates unnecessary searches** - we can determine search direction
- **Successor definition maps to BST property** - smallest value > p.val
- **Single path traversal possible** instead of exploring entire tree

Key insights:
- Naive approach requires O(n) inorder traversal to find all nodes in order
- BST property allows direct search for "smallest greater value" in O(h) time
- When current.val > p.val, current is a candidate, but we search left for better candidates
- When current.val <= p.val, we must search right since left subtree has smaller values

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `root = [2,1,3], p = 1` | Successor exists (next in inorder) | `2` |
| `root = [5,3,6,2,4,null,null,1], p = 6` | No successor (p is maximum) | `null` |
| `root = [2,1,3], p = 2` | Successor exists (right child) | `3` |
| `root = [5,3,6,2,4], p = 3` | Successor in right subtree of p | `4` |
| `root = [1], p = 1` | Single node tree | `null` |

These test:
- Standard successor cases where next node exists
- Edge case where p is the maximum value (no successor)
- Cases where successor is immediate right child
- Cases where successor is in subtree but not immediate child
- Minimal tree edge case

## ☀️ Code

### Solution 1: Brute Force - Complete Inorder Traversal (Brute Force)
**Time: O(n) → Must traverse entire tree to build inorder list**  
**Space: O(n) → Store all node values in list**

```python
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        def inorder(node):
            """Collect all nodes using inorder traversal"""
            if not node:
                return []
            
            result = []
            result.extend(inorder(node.left))   # Left subtree
            result.append(node)                 # Current node
            result.extend(inorder(node.right))  # Right subtree
            
            return result
        
        # Get all nodes in sorted order
        nodes = inorder(root)
        
        # Find p and return next node
        for i in range(len(nodes)):
            if nodes[i] == p:
                return nodes[i + 1] if i + 1 < len(nodes) else None
        
        return None
```

### Solution 2: BST Property with Iterative Search (Classic Solution)
**Time: O(h) → Best case O(log n), worst case O(n) for skewed tree**  
**Space: O(1) → Only constant extra space**

```python
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        current = root
        
        while current:
            # If current value is greater than p's value,
            # it could be a potential successor
            if current.val > p.val:
                successor = current  # Update potential successor
                current = current.left  # Look for smaller successor in left subtree
            else:
                # If current value is <= p's value, successor must be in right subtree
                current = current.right
        
        return successor
```

### Solution 3: Two-Case BST Logic (Advanced Solution)
**Time: O(h) → Best case O(log n), worst case O(n) for skewed tree**  
**Space: O(1) → Only constant extra space**

```python
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # Case 1: p has right subtree - successor is leftmost node in right subtree
        if p.right:
            current = p.right
            while current.left:
                current = current.left
            return current
        
        # Case 2: p has no right subtree - find ancestor where p is in left subtree
        successor = None
        current = root
        
        while current:
            if p.val < current.val:
                successor = current  # current could be the successor
                current = current.left
            elif p.val > current.val:
                current = current.right
            else:
                # Found p, but it has no right subtree (handled in case 1)
                break
        
        return successor
```

## ☀️ Notes

**Key Algorithm Components:**
- BST property utilization for efficient search direction
- Successor candidate tracking during tree traversal
- Optimal path selection to minimize comparisons
- Proper handling of cases where no successor exists

**Critical Insight:**
The power of Solution 2 lies in its elegant use of BST ordering. Instead of finding all nodes and looking for the next one, we directly search for the smallest value greater than p.val by maintaining the best candidate seen so far and continuing to search for potentially better (smaller) candidates.

## ☀️ Coding Walkthrough Script

"I'll solve this by leveraging the BST property to directly search for the successor without needing to traverse the entire tree.

The key insight is that the inorder successor of p is simply the smallest node with value greater than p.val. Instead of doing a complete inorder traversal, I can use the BST structure to search efficiently.

I'll maintain a 'successor' variable to track the best candidate found so far, starting from null. I traverse the tree starting from root using a simple while loop.

At each node, I check if the current value is greater than p's value. If so, this node is a potential successor, so I update my successor variable. But since I want the smallest such value, I continue searching in the left subtree to see if there's an even smaller successor.

If the current value is less than or equal to p's value, I know that all nodes in the left subtree will also be smaller than or equal to p's value, so the successor must be in the right subtree.

This approach is elegant because it follows a single path through the tree, making exactly the right decisions at each node based on the BST property.

The time complexity is O(h) where h is the tree height, giving us O(log n) for balanced trees, which is much better than the O(n) required for complete traversal."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Complete Inorder | O(n) | O(n) | Build full sorted list | Simple but inefficient |
| BST Iterative Search | O(h) | O(1) | Direct search for smallest > p.val | **Recommended**; optimal |
| Two-Case Logic | O(h) | O(1) | Handle right subtree vs ancestor cases | More complex but instructive |

## ☀️ BST Successor Insights

- **Successor definition:** Smallest node with value greater than target
- **BST advantage:** Ordering property eliminates need for complete traversal
- **Search strategy:** When candidate found, search left for potentially better candidates
- **Edge case handling:** Maximum value node has no successor
- **Two successor scenarios:** Right subtree minimum or ancestor relationship

**Mathematical Guarantee:** Since BST maintains left < root < right ordering, the algorithm's search strategy of going left when current > target and right when current <= target will find the smallest value greater than target if one exists.
