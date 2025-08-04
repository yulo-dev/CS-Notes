
# Leetcode 234. Palindrome Linked List

## Tags
Linked List, Two Pointers

---

## ☀️ UMPIRE

### U — Understand
- Given the head of a singly linked list, return `True` if it is a palindrome.
- Otherwise, return `False`.

#### Clarifying Questions
1. Can the linked list be empty? → Yes, return True.
2. What if there is only one node? → Return True.
3. Can we modify the linked list? → For the O(1) space solution, yes.

---

### M — Match
Common approaches for palindrome:
1. Convert linked list to array → Two pointers compare.
2. Use fast & slow pointers → Find midpoint, reverse second half, compare.

---

### P — Plan

#### Approach 1: Convert to Array (Easy to implement)
1. Traverse linked list, store values in array.
2. Use two pointers (left, right) to check palindrome.

#### Approach 2: O(1) Extra Space (Fast & Slow Pointer + Reverse)
1. **Find middle node** using fast & slow pointers.
2. **Reverse second half** of the linked list.
3. **Compare** first half and reversed second half.
4. (Optional) Restore list if modification is not allowed.

---

### I — Implement

#### Approach 1: Array
```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Convert linked list to array
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next

        # Two pointers check
        left, right = 0, len(values) - 1
        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1

        return True
```
- **Time:** O(n)
- **Space:** O(n)

#### Approach 2: Fast & Slow + Reverse
```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Edge case: 0 or 1 node → palindrome
        if not head or not head.next:
            return True

        # Step 1: Find middle (slow = mid)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        # Step 3: Compare first half and reversed second half
        left = head
        right = prev
        while right:  # only need to traverse half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
```
- **Time:** O(n)
- **Space:** O(1) (in-place reverse)

---

### R — Review
- Handle edge cases: empty list, single node.
- Understand pointer manipulation in reverse:
  - `nxt = slow.next` → save next node
  - `slow.next = prev` → reverse pointer
  - `prev = slow` → advance prev
  - `slow = nxt` → move to next node

---

### E — Evaluate
- Array method is simple but needs O(n) extra memory.
- Fast & slow pointer + reverse is optimal:
  - Only O(1) space
  - In-place operation

---

## ☀️ Key Takeaways
- **Linked List traversal** needs `while` loop and manual pointer movement (`node = node.next`).

---

## ☀️ Script

### Approach 1 (Array)
1. First, traverse the linked list and store all node values in an array.
2. Then, use two pointers: one at the start and one at the end.
3. Move inward while comparing values at both ends.
4. If any mismatch is found, return False immediately.
5. If all values match, return True.

### Approach 2 (Fast & Slow Pointer + Reverse)
1. Handle edge cases: if the list is empty or has only one node, return True.
2. Use fast and slow pointers to find the midpoint: slow moves one step, fast moves two.
3. Reverse the second half of the list in place using three pointers: `prev`, `slow`, and `nxt`.
4. Compare nodes from the start of the list and from the head of the reversed second half.
5. If a mismatch is found, return False.
6. If all compared nodes match, return True.
