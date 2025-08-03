# Leetcode 876. Middle of the Linked List

**Tags:** Linked List, Two Pointers

---

## ☀️ UMPIRE

### U — Understand
- Given the head of a singly linked list, return the **middle node**.
- If there are two middle nodes (even length), return the **second** one.

**Clarifying Questions:**
- Can the list be empty? → Yes, return None.
- If there is one node? → Return that node itself.
- Do we modify the list? → No, just return the node reference.

---

### M — Match
- Linked List problem → common patterns:
  - **Count length and re-traverse** (basic, two passes)
  - **Fast & slow pointers** (optimal, one pass)

---

### P — Plan

#### Approach 1: Count Length (Basic)
1. Traverse the linked list to count its length `L`.
2. Compute middle index `L // 2`.
3. Traverse again to the middle node.
4. Return it.

#### Approach 2: Fast & Slow Pointers (Optimal)
1. Initialize two pointers slow and fast at head.
2. Move slow by one step, fast by two steps.
3. When fast reaches end (`None`), slow is at the middle.
4. Return slow.

---

### I — Implement

#### Approach 1: Count Length
```python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: count length
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Step 2: move to middle node
        middle_index = length // 2
        current = head
        for _ in range(middle_index):
            current = current.next
        
        return current
```

#### Approach 2: Fast & Slow Pointers (Recommended)
```python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize slow and fast pointers
        slow = fast = head
        
        # Move fast by two steps and slow by one step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # When fast reaches the end, slow is at the middle
        return slow
```

---

### R — Review

#### Time Complexity
- Count length → O(n) (two traversals)
- Fast & slow → O(n) (one traversal)
- Array → O(n)

#### Space Complexity
- Count length → O(1)
- Fast & slow → O(1)
- Array → O(n)

---

### E — Evaluate

#### Why fast & slow pointer?
- Only needs one pass and constant extra space.
- Automatically returns the **second** middle node in even-length lists.

#### Why does count length need two passes?
- Linked List **cannot directly access length or index** like arrays.
- Must first traverse to count length, then traverse again to reach middle.

#### Other solutions
- Array method is straightforward but wastes O(n) memory.
- Recursion works but is not practical due to call stack limits.

---

## ☀️ Script

The simplest way is to first traverse the list to count its length, then traverse again to the middle — O(n) time, O(1) space, but requires two passes.  
A better approach is to use two pointers: slow moves one step and fast moves two steps. When fast reaches the end, slow is at the middle. This naturally returns the second middle node for even-length lists.  
Both approaches are O(n) time and O(1) space, but the fast & slow pointer method is more efficient since it only needs one pass. Another possible solution is storing nodes in an array, but that takes O(n) space.
