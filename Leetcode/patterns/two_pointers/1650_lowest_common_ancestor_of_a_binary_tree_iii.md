
# Leetcode 1650 - Lowest Common Ancestor of a Binary Tree III

## ☀️ UMPIRE

### Understand:
- **Input**: Two given nodes `p` and `q` from the same tree, where each node has a pointer to its parent.
- **Output**: Return their lowest common ancestor (LCA).
- **Definition**: LCA is defined as the lowest node that has both `p` and `q` as descendants (a node can be a descendant of itself).
- **Constraints**:  
  - All nodes are part of the same connected tree.  
  - The tree has no cycles.  
  - Each node has a `parent` pointer.  
- **Goal**: Find the LCA efficiently without traversing the entire tree from the root.

### Match:
- **Category**: Tree traversal & ancestor lookup.
- **Patterns**:  
  - Method 1: Ancestor recording with a hash set (space trade-off).  
  - Method 2: Two Pointers (Linked List Intersection style) → Optimal space O(1).

### Plan:
**Method 1: Ancestor Set**
1. Walk upward from node `p`, storing all ancestors in a set.
2. Walk upward from node `q`, returning the first node found in that set.

**Method 2 (Preferred): Two Pointers**
1. Initialize two pointers `a = p` and `b = q`.
2. Move each pointer upward step by step.
3. When a pointer reaches the root (None), redirect it to the other node’s starting point.
4. Continue until `a == b`. The intersection node is the LCA.

### Review:
- Are we handling the case where one node is an ancestor of the other? (Handled: will meet in first loop)
- Are we handling the case where nodes are identical? (Handled: while loop exits immediately)
- Is there any risk of infinite loop? (No, because total steps are limited to `p→root + q→root`)

### Evaluate:
- **Method 1**:
  - Time: O(h) (h = tree height)
  - Space: O(h) (for storing ancestors)
- **Method 2**:
  - Time: O(h)
  - Space: O(1) (no extra storage)

---

## ☀️ Code (Method 1: Ancestor Set)
```python
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ancestors = set()
        # Record all ancestors of p
        while p:
            ancestors.add(p)
            p = p.parent
        # Find first common ancestor from q's lineage
        while q:
            if q in ancestors:
                return q
            q = q.parent
        return None  # Should never be reached in a valid tree
```

---

## ☀️ Code (Method 2: Two Pointers - Recommended)
```python
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a, b = p, q
        while a != b:
            # When reaching the root, switch to the other node
            a = a.parent if a else q
            b = b.parent if b else p
        return a
```

---

## ☀️ Coding Walkthrough Script
1. **Initialize two pointers**: `a` starts at `p`, `b` starts at `q`.
2. **Traverse upward**: each step moves one level up toward the root.
3. **Handle depth difference**:
   - If one pointer reaches None (past the root), it jumps to the other node’s starting point.
   - This ensures both pointers travel the same total distance: `p→root + q→root`.
4. **Meeting point**:
   - They will eventually meet at the first common node in their upward paths.
   - That node is guaranteed to be the Lowest Common Ancestor (LCA).

---

## ☀️ Complexity Comparison
| Method      | Time Complexity | Space Complexity | Notes |
|-------------|----------------|------------------|-------|
| Ancestor Set | O(h)           | O(h)             | Uses extra memory to store ancestors |
| Two Pointers | O(h)           | O(1)             | No extra memory; elegant and commonly expected in interviews |

---

## ☀️ Edge Cases
- **Same Node**: `p == q` → returns `p` immediately.
- **One Node is Ancestor**: if `p` is an ancestor of `q` → returns `p` in the first loop.
- **Different Depth**: nodes at different depths → handled by pointer swapping.
- **Worst Case (Only root in common)**: still works, returns root.

---

## ☀️ Key Insights
- A tree always has unique upward paths to the root → ensures eventual convergence.
- The two-pointer approach is inspired by the linked list intersection pattern (Leetcode 160).
- First intersection point when traveling equal total distances must be the LCA.
