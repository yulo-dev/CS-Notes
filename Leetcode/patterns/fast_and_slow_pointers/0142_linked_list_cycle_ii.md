
# Leetcode 142: Linked List Cycle II

## Problem
Given the head of a linked list, return the node where the cycle begins.  
If there is no cycle, return `None`.  

A cycle in a linked list occurs if a node can be reached again by continuously following the `next` pointer.  
Do not modify the linked list.

---

## UMPIRE

### Understand
- **Input**: head of linked list (could be empty)
- **Output**: node where cycle begins, or None if no cycle
- **Constraints**:
  - The linked list might have no cycle.
  - If a cycle exists, there is exactly one cycle entry.

### Match
- Detect cycle → common patterns:
  1. **HashSet** to store visited nodes.
  2. **Floyd's Cycle Detection** (Tortoise and Hare) → O(1) space.

### Plan

#### Approach 1: HashSet
1. Traverse the list, keep track of visited nodes.
2. If a node is visited twice, return it (cycle entry).
3. If reach the end (`None`), no cycle → return None.

#### Approach 2: Floyd’s Tortoise and Hare
1. Use two pointers (`slow`, `fast`) to detect cycle:
   - `slow` moves one step, `fast` moves two steps.
   - If they meet, a cycle exists.
2. Reset one pointer to head.
3. Move both pointers one step at a time:
   - The node where they meet again is the cycle entry.

---

## Implement

### Solution 1: HashSet (O(n) space)
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        current = head
        
        while current:
            if current in visited:
                return current  # cycle entry
            visited.add(current)
            current = current.next
        
        return None  # no cycle
```

### Solution 2: Floyd’s Tortoise and Hare (O(1) space)
```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: detect if cycle exists
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:  # cycle detected
                # Step 2: find cycle entry
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow  # cycle entry
        
        return None  # no cycle
```

---

## Review

**Time Complexity**:
- Approach 1: O(n)
- Approach 2: O(n)

**Space Complexity**:
- Approach 1: O(n)
- Approach 2: O(1)

---

## Evaluate
- Approach 1 is simple, easy to implement but uses extra space.
- Approach 2 is optimal, using constant extra space and is the recommended interview solution.

---

## Script (self-narration while coding)
I’ll first handle a simple solution by storing visited nodes in a HashSet.  
If I revisit a node, I immediately return it as the cycle entry.  
This gives me O(n) time and O(n) space.  
For the optimal solution, I use Floyd’s cycle detection.  
I move two pointers: slow (1 step) and fast (2 steps). If they meet, there’s a cycle.  
Then I reset one pointer to head and move both one step at a time until they meet again.  
The node where they meet is the cycle entry.  
This approach is O(n) time and O(1) space.
