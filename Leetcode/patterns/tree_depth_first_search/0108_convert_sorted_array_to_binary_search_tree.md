# Leetcode 0108 - Convert Sorted Array to Binary Search Tree

## ☀️ UMPIRE

**Understand:** Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree. A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

**Match:** This is a Divide and Conquer problem using recursive tree construction. The key insight is that by always choosing the middle element as the root, we can guarantee both BST property (due to sorted input) and height balance (due to equal left/right subtree sizes).

**Plan:**
1. Choose the middle element of current range as root
2. Recursively build left subtree from left half of array  
3. Recursively build right subtree from right half of array
4. Use index pointers to avoid array slicing overhead
5. Base case: when left index > right index, return null

**Implement:** See the code section below.

**Review:**
- Ensure we maintain BST property (left < root < right)
- Verify that tree remains height-balanced at all levels
- Check that we handle empty array and single element cases
- Confirm optimal time complexity without unnecessary array operations

**Evaluate:**
- Time: O(n) - visit each array element exactly once to create nodes
- Space: O(log n) - recursion stack depth for balanced tree

## ☀️ Why This Is a Divide and Conquer Problem

Converting sorted array to balanced BST naturally fits divide and conquer pattern:
- **Input is pre-sorted** - eliminates need for sorting or complex balancing operations
- **Middle element choice guarantees balance** - equal-sized left and right subtrees
- **Recursive subproblem structure** - each subtree is independently constructed
- **Optimal substructure** - balanced subtrees combine to form balanced tree

Key insights:
- Brute force with array slicing has O(n log n) overhead due to array copying
- Index-based approach achieves O(n) by avoiding array operations
- Middle element selection ensures O(log n) height for resulting tree
- Divide and conquer naturally maintains both BST and balance properties

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `nums = [-10,-3,0,5,9]` | Standard sorted array | Balanced BST with root 0 |
| `nums = [1,3]` | Two elements | BST with either as root |
| `nums = []` | Empty array | `null` |
| `nums = [5]` | Single element | Single node tree |
| `nums = [1,2,3,4,5,6,7]` | Odd length perfect case | Perfectly balanced BST |
| `nums = [1,2,3,4]` | Even length | Balanced BST (left or right bias) |

These test:
- Standard conversion scenarios
- Minimal input sizes
- Empty array boundary condition
- Single node edge case
- Perfect balance cases with odd/even lengths

## ☀️ Code

### Solution 1: Brute Force with Array Slicing (Brute Force)
**Time: O(n log n) → O(n) for each level * O(log n) levels, plus array slicing overhead**  
**Space: O(n log n) → Array slicing creates new arrays at each recursive call**

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        # Find middle element as root to ensure balance
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        
        # Recursively build left and right subtrees with array slicing
        root.left = self.sortedArrayToBST(nums[:mid])      # Left half
        root.right = self.sortedArrayToBST(nums[mid+1:])   # Right half
        
        return root
```

### Solution 2: Optimized Recursive with Index Pointers (Classic Solution)
**Time: O(n) → Visit each element exactly once to create nodes**  
**Space: O(log n) → Recursion stack depth for balanced tree**

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            # Base case: no elements to process
            if left > right:
                return None
            
            # Choose middle element as root to maintain balance
            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            
            # Recursively build left and right subtrees
            root.left = build(left, mid - 1)      # Left half
            root.right = build(mid + 1, right)    # Right half
            
            return root
        
        return build(0, len(nums) - 1)
```

### Solution 3: Iterative with Stack (Advanced Solution)
**Time: O(n) → Visit each element exactly once to create nodes**  
**Space: O(n) → Stack storage for iterative processing**

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        # Stack stores (left_index, right_index, parent_node, is_left_child)
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        stack = [(0, mid - 1, root, True), (mid + 1, len(nums) - 1, root, False)]
        
        while stack:
            left, right, parent, is_left = stack.pop()
            
            if left > right:
                continue
                
            mid = left + (right - left) // 2
            node = TreeNode(nums[mid])
            
            if is_left:
                parent.left = node
            else:
                parent.right = node
            
            # Add subtrees to stack
            stack.append((left, mid - 1, node, True))
            stack.append((mid + 1, right, node, False))
        
        return root
```

## ☀️ Notes

**Key Algorithm Components:**
- Middle element selection for guaranteed balance
- Index-based recursion to avoid array copying overhead
- Divide and conquer pattern with BST construction
- Base case handling for empty ranges

**Critical Insight:**
The elegance of this solution comes from leveraging the pre-sorted input. Since the array is already sorted, choosing the middle element as root automatically satisfies both BST property (left elements < root < right elements) and balance property (equal-sized subtrees).

## ☀️ Coding Walkthrough Script

"I'll solve this using divide and conquer with index pointers for optimal efficiency.

The key insight is that since the input array is already sorted, I can guarantee both BST property and height balance by always choosing the middle element as the root.

I'll use a helper function that takes left and right indices instead of creating new arrays. This avoids the expensive array slicing operations that would make the solution O(n log n).

For each recursive call, I find the middle index using the formula mid = left + (right - left) // 2. This avoids potential integer overflow compared to (left + right) // 2.

I create a new TreeNode with the middle element's value, then recursively build the left subtree using elements from left to mid-1, and the right subtree using elements from mid+1 to right.

The base case is when left > right, meaning there are no elements in the current range, so I return null.

This approach ensures that at every level, the left and right subtrees have roughly equal sizes, guaranteeing a height-balanced tree. Since the input is sorted, the BST property is automatically satisfied.

The time complexity is O(n) because I visit each array element exactly once to create a tree node. The space complexity is O(log n) for the recursion stack in a balanced tree."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| Array Slicing | O(n log n) | O(n log n) | Recursive with array copying | Simple but inefficient |
| Index Pointers | O(n) | O(log n) | Recursive with index bounds | **Recommended**; optimal |
| Iterative Stack | O(n) | O(n) | Stack-based tree construction | Avoids recursion limits |

## ☀️ Tree Construction Insights

- **Balance guarantee:** Middle element selection ensures equal-sized subtrees
- **BST property:** Pre-sorted input automatically satisfies left < root < right
- **Divide and conquer:** Each subproblem is an independent, smaller version
- **Optimization opportunity:** Index pointers eliminate expensive array operations
- **Height guarantee:** Resulting tree has O(log n) height for O(n) elements

**Mathematical Guarantee:** Since we always split the array into two equal (or nearly equal) halves and the input is pre-sorted, the resulting tree will have height at most ⌈log₂(n+1)⌉, ensuring optimal balance.
