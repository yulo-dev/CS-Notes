# Leetcode 116 - Populating Next Right Pointers in Each Node

## ☀️ UMPIRE

**Understand:** Given a perfect binary tree, populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL. A perfect binary tree is a binary tree where all interior nodes have two children and all leaves are at the same level.

**Key Clarification Questions to Ask Interviewer:**
1. "Since this is guaranteed to be a perfect binary tree, can I leverage this constraint for optimization?"
2. "Is O(1) extra space complexity preferred over O(n), or is any approach acceptable?"
3. "Should I modify the tree in-place, or is it acceptable to use additional data structures?"
4. "Are there any constraints on the tree size that would affect the approach choice?"

**Match:** This is a tree level-order processing problem with a key constraint: perfect binary tree structure allows for space optimization.

"When I see 'populate next pointers' with 'perfect binary tree', I recognize this as a level-order traversal problem with a special optimization opportunity. The perfect binary tree constraint is crucial - it means every level is completely filled, which allows me to use existing next pointers to traverse levels without additional space.

While BFS naturally handles level-by-level processing, the perfect binary tree property enables an elegant O(1) space solution. I can use the next pointers I've already established in the current level to connect nodes in the next level.

My plan is to start with BFS to ensure correctness, then optimize to the O(1) space solution that leverages the perfect binary tree structure."

**Plan:**
1. Handle null root edge case
2. Use level-by-level processing to connect nodes at each level
3. For BFS: use queue and previous pointer technique
4. For optimization: use existing next pointers to traverse current level while connecting next level
5. Continue until all levels are processed

**Implement:** See the code section below.

**Review:**
- Edge case: Empty tree returns as-is
- Edge case: Single node (no connections needed)
- Perfect binary tree constraint: every level is completely filled
- Connection correctness: each node points to its right neighbor or null

**Evaluate:**
- Time: O(n) - Visit each node once
- Space: BFS O(n), Optimized O(1)

## ☀️ Why This Is a Level-Order Processing Problem with Optimization

Populating next pointers requires connecting nodes at the same level, which naturally suggests level-order traversal. However, the perfect binary tree constraint provides a crucial optimization opportunity - we can use already-established next pointers to traverse levels without additional space.

Key insights:
- Level-order connection pattern requires processing complete levels
- Perfect binary tree means every level is completely filled
- Once we establish next pointers at level k, we can use them to traverse level k while connecting level k+1
- This eliminates the need for a queue after the first level

## ☀️ Edge Case Notes

| Input | Description | Expected Output |
|-------|-------------|-----------------|
| `null` | Empty tree | `null` |
| `Node(1)` | Single node | `Node(1)` with next=null |
| `[1,2,3,4,5,6,7]` | Perfect tree | All nodes connected to right neighbors |

These test:
- Null input boundary condition
- Single node (no siblings to connect)
- Standard perfect binary tree with multiple levels

## ☀️ Code

### Solution 1: BFS with Previous Pointer (Brute Force)

**Time: O(n) → Visit each node once in level order traversal**
**Space: O(w) → O(n) worst case, where w is max width of tree level**

```python
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
```

### Solution 2: O(1) Space Using Existing Pointers (Classic Solution)

**Time: O(n) → Visit each node once using level-by-level iteration**
**Space: O(1) → Only use pointers, no additional data structures**

```python
def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
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
```

### Solution 3: Recursive DFS Approach (Advanced Solution)

**Time: O(n) → Visit each node once in recursive calls**
**Space: O(h) → where h is the height; for a perfect binary tree h = O(log n)**

```python
def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
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
```

## ☀️ Notes

**Key Algorithm Components:**
- Level-by-level processing for connecting same-level nodes
- Perfect binary tree constraint enables O(1) space optimization
- Using established next pointers to traverse current level while building next level

**Critical Insight:**
The perfect binary tree constraint is the key to optimization. It guarantees that we can use established next pointers to traverse levels without additional storage, transforming an O(n) space problem into O(1) space.

## ☀️ Coding Walkthrough Script

"I need to connect each node to its next right node in a perfect binary tree. This is fundamentally a level-order processing problem, but the perfect binary tree constraint gives me a crucial optimization opportunity.

My first approach would be BFS using a queue, where I process each level completely and use a previous pointer to connect nodes as I process them. This gives me O(n) time and O(n) space complexity.

However, the perfect binary tree property allows for a much better solution. Since every level is completely filled, once I establish next pointers at level k, I can use those pointers to traverse level k while simultaneously connecting the nodes at level k+1. This eliminates the need for a queue entirely.

For the optimized solution, I use two pointers: leftmost tracks the leftmost node of each level, and head traverses the current level using next pointers. As I traverse each level, I connect the children: each node's left child connects to its right child, and each node's right child connects to the next node's left child.

Time complexity remains O(n) since I visit each node once, but space complexity drops to O(1) since I only use a constant number of pointers regardless of tree size."

## ☀️ Solution Comparison

| Method | Time Complexity | Space Complexity | Key Strategy | Notes |
|--------|----------------|------------------|--------------|-------|
| BFS with Prev | O(n) | O(w) → O(n) | Level-by-level with queue | Clear but not optimal |
| O(1) Space Pointers | O(n) | O(1) | Use existing connections | **Recommended** |
| Recursive DFS | O(n) | O(log n) | Connect during traversal | Elegant recursive solution |

## ☀️ Perfect Binary Tree Insights

- Perfect binary tree constraint enables significant space optimization
- Level-by-level problems can often be optimized when tree structure is guaranteed
- Using established pointers to traverse current level while building next level is a powerful technique
- O(1) space solutions often require leveraging problem constraints creatively

**Mathematical Guarantee:** In a perfect binary tree, every level is completely filled, allowing us to use established next pointers for traversal without additional storage.

**Note:** Solution 2 is recommended because it demonstrates the key insight of leveraging problem constraints for optimization, achieving O(1) space complexity while maintaining clear, readable code.
