# 141. Linked List Cycle

**Tags:** Linked List, Hash Table, Two Pointers, Floyd's Cycle Detection

---

## Problem
Given the `head` of a linked list, determine if the linked list has a cycle in it.

A cycle exists if there is a node in the linked list that can be reached again by continuously following the `next` pointer.

Return `True` if there is a cycle in the linked list, otherwise return `False`.

**Example:**  
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle connecting tail node to node index 1.
```
--

## ☀️ UMPIRE

### U — Understand
- We are given the head of a singly linked list.
- A cycle exists if a node's `.next` eventually points to a previous node (loop).
- Return `True` if there is a cycle, `False` otherwise.

**Clarifying Questions:**
- Can the list be empty? → Yes. If head is `None`, return `False`.
- Is it singly linked or doubly? → Singly.
- Do we need to find where the cycle starts? → No, just detect if it exists.

---

### M — Match
- This is a classic **Cycle Detection** problem.
- Two common patterns:
  1. **HashSet to track visited nodes** (extra space)
  2. **Fast & slow pointer (Floyd’s Tortoise and Hare)** — O(1) space
- Similar to:
  - Leetcode 202 (Happy Number)
  - Leetcode 142 (Linked List Cycle II)
  - Leetcode 287 (Find the Duplicate Number)

---

### P — Plan

#### Approach 1: HashSet
- Traverse the list while storing each visited node.
- If we revisit a node, there's a cycle.
- If we reach the end (None), return False.

#### Approach 2: Fast & Slow Pointers
- Use two pointers:
  - Slow moves one step
  - Fast moves two steps
- If there is a cycle, they will eventually meet.
- If fast reaches None → no cycle

---

## Approach 1: HashSet

### Idea
- Use a HashSet to keep track of all visited nodes.
- If we encounter a node that has already been visited, a cycle exists.
- If we reach the end (`None`), there is no cycle.

### Code
```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Set to store visited nodes
        seen = set()
        current = head

        # Traverse the linked list one step at a time
        while current:
            # If current node is already seen, cycle detected
            if current in seen:
                return True
            seen.add(current)
            current = current.next

        # If traversal ends (no cycle)
        return False
```

### Complexity
- **Time:** O(n) – each node is visited at most once  
- **Space:** O(n) – need to store visited nodes in a set

---

## Approach 2: Fast & Slow Pointers (Floyd's Cycle Detection)

### Idea
- Use two pointers: slow moves one step, fast moves two steps.
- If there is a cycle, they will eventually meet inside the cycle.
- If `fast` or `fast.next` becomes `None`, the linked list has no cycle.

### Code
```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers
        slow = fast = head

        # Continue while fast pointer and next node are valid
        while fast and fast.next:
            slow = slow.next           # Move slow pointer by 1
            fast = fast.next.next      # Move fast pointer by 2

            # If slow and fast meet, there is a cycle
            if slow == fast:
                return True

        # If fast reached the end, no cycle
        return False
```

### Complexity
- **Time:** O(n) – pointers traverse at most n nodes  
- **Space:** O(1) – no extra data structures used

---

## Why Different While Conditions?

### HashSet Approach → `while current`
- Only moves **one step** each iteration (`current = current.next`).
- We only need to check if the **current node** exists, no risk of accessing `None.next`.
- Loop ends naturally when `current` becomes `None`.

### Fast & Slow Pointer Approach → `while fast and fast.next`
- Fast pointer moves **two steps** each iteration (`fast = fast.next.next`).
- Must ensure both `fast` and `fast.next` are not `None` to avoid runtime error.
- Ensures safe pointer movement in each loop iteration.

---

## Script (Fast & Slow Pointers)
We initialize two pointers, slow and fast, both pointing to the head.  
In each loop, slow moves one step, while fast moves two steps.  
If there is no cycle, the fast pointer will eventually reach the end (`None`) and the loop ends.  
If there is a cycle, eventually the fast pointer will lap the slow pointer, and they will meet, confirming the cycle.  
This algorithm runs in O(n) time and O(1) space, making it optimal.
