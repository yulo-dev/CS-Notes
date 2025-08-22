# Leetcode 0230 - Kth Smallest Element in a BST

## ☀️ UMPIRE

**Understand:** Given the root of a binary search tree and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree. We need to find the kth element when all node values are arranged in ascending order.

**Match:** This is a Tree Traversal problem that leverages BST properties using DFS (Depth-First Search). The key insight is that inorder traversal of a BST produces values in sorted order, so the kth smallest element is simply the kth element encountered during inorder traversal.

**Plan:**
1. Use inorder traversal to visit nodes in ascending order
2. Count nodes as we visit them during traversal
3. When we reach the kth node, that's our answer
4. Use early termination to avoid unnecessary traversal

**Implement:** See the code section below.

**Review:**
- Ensure we're doing inorder traversal correctly (left → root → right)
- Verify that we handle k being 1-indexed properly
- Check that early termination works to stop unnecessary traversal
- Confirm we handle edge cases like k = 1 and k = total nodes

**Evaluate:**
- Time: O(h + k) - best case O(log n + k), worst case O(n) when k = n
- Space: O(h) where h is tree height - recursion stack depth

## ☀️ Why This Is a BST Inorder Traversal Problem

BST has a special property that makes this problem elegant:
- **Inorder traversal of BST produces sorted sequence** (left → root → right)
- **Kth smallest = kth element in inorder sequence**
- **Early termination possible** since we don't need the entire sorted list
- **No external sorting required** due to BST structure

Key insights:
- BST inorder traversal naturally gives us elements in ascending order
- We can stop as soon as we find the kth element (no need to visit remaining nodes)
- This is much more efficient than extracting all values and sorting
- The tree structure allows us to skip entire subtrees once we find our answer

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `root = [3,1,4,null,2], k = 1` | Find 1st smallest | `1` |
| `root = [5,3,6,2,4,null,null,1], k = 3` | Find 3rd smallest | `3` |
| `root = [1], k = 1` | Single node tree | `1` |
| `root = [2,1,3], k = 3` | Find largest element | `3` |
| `root = [5,3,6,2,4], k = 4` | Find 4th in larger tree | `5` |

These test:
- Different positions of k (first, middle, last)
- Single node edge case
- Trees of varying sizes and structures
- Validation that inorder gives correct sorted sequence

## ☀️ Code

### Solution 1: Brute Force - Complete Inorder Traversal (Brute Force)
**Time: O(n) → Visit all nodes to build complete sorted list**  
**Space: O(n) → Store all node values in list**

```python
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
```

### Solution 2: Optimized Inorder with Countdown (Classic Solution)
**Time: O(h + k) → Best case O(log n + k), worst case O(n) when k = n**  
**Space: O(h) → Recursion stack depth equals tree height**

```python
class Solution:
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
```

### Solution 3: Iterative Inorder with Stack (Advanced Solution)
**Time: O(h + k) → Best case O(log n + k), worst case O(n) when k = n**  
**Space: O(h) → Stack storage for iterative traversal**

```python
class Solution:
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
```

## ☀️ Notes

**Key Algorithm Components:**
- Inorder traversal pattern: left → process → right
- Countdown mechanism to track remaining nodes to visit
- Early termination when target is found
- Proper handling of 1-indexed k value

**Critical Insight:**
The power of this solution comes from leveraging the fundamental BST property: inorder traversal produces a sorted sequence. This eliminates the need for explicit sorting and allows for elegant early termination.

## ☀️ Coding Walkthrough Script

I'll solve this by leveraging the key property of BSTs: inorder traversal gives us values in sorted order.
My approach uses a countdown strategy. I start with k representing how many more nodes I need to visit to reach my target. As I perform inorder traversal, I decrement k each time I visit a node.
The inorder traversal follows the classic left-root-right pattern: first I traverse the left subtree to visit all smaller values, then I process the current node by decrementing k, and finally I check if this is my target.
When k reaches 0, I've found the kth smallest element and can return immediately without visiting the rest of the tree. This early termination is crucial for efficiency.
The time complexity is O(h + k) where h is the tree height, since in the best case I only need to traverse down to a leaf and then visit k nodes. The space complexity is O(h) for the recursion stack.
This approach is optimal because it leverages the BST structure to avoid any explicit sorting while still giving us elements in the correct order."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Complete Inorder | O(n) | O(n) | Build full sorted list | Simple but memory inefficient |
| Optimized Countdown | O(h + k) | O(h) | Early termination with countdown | **Recommended**; optimal for most cases |
| Iterative Stack | O(h + k) | O(h) | Avoid recursion overhead | Good for avoiding recursion limits |

## ☀️ BST Kth Element Insights

- **BST fundamental property:** Inorder traversal = sorted sequence
- **Optimization opportunity:** Stop early when target is found
- **Countdown intuition:** "How many more do I need?" is more natural than "How many have I seen?"
- **Time complexity benefit:** When k << n, we visit much fewer than n nodes
- **Space efficiency:** No need to store intermediate results

**Mathematical Guarantee:** Since BST inorder traversal mathematically guarantees sorted order, the kth node visited during inorder traversal is definitively the kth smallest element in the tree.
