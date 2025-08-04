# Leetcode 2130: Maximum Twin Sum of a Linked List

## Problem
Given the head of a linked list with even length, return the maximum twin sum of the linked list.

A twin sum is defined as the sum of the ith node and the (n-i-1)th node (0-indexed).

---

## UMPIRE

### Understand
- Input: head of linked list (even length)
- Output: maximum twin sum
- Constraints:
  - Length of linked list is even
  - Node values are integers

### Match
- Linked list problem
- Approaches:
  1. Convert linked list to array (simpler)
  2. O(1) space: find middle, reverse second half, compare

### Plan
#### Approach 1: Array + Two Pointers
1. Traverse the linked list and store values in an array.
2. Use two pointers (one from start, one from end) to compute twin sums.
3. Return the maximum twin sum.

#### Approach 2: O(1) Space (Find Mid + Reverse Second Half)
1. Use fast & slow pointers to find middle of the list.
2. Reverse the second half of the linked list.
3. Use two pointers (one from head, one from reversed list) to compute twin sums.
4. Return the maximum twin sum.

### Implement

#### Solution 1: Array + Two Pointers
```python
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Convert linked list to array
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        # Two pointers from both ends
        left, right = 0, len(values) - 1
        max_sum = 0
        while left < right:
            max_sum = max(max_sum, values[left] + values[right])
            left += 1
            right -= 1

        return max_sum
```

#### Solution 2: Fast and Slow Pointers + Reverse Second Half
```python
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find middle node
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # Compare twin sums
        max_sum = 0
        left, right = head, prev
        while right:
            max_sum = max(max_sum, left.val + right.val)
            left = left.next
            right = right.next

        return max_sum
```
---

### Review
**Time Complexity:**
- Approach 1: `O(n)`
- Approach 2: `O(n)`

**Space Complexity:**
- Approach 1: `O(n)`
- Approach 2: `O(1)`

### Evaluate
- Approach 1 is simpler, suitable for quick implementation.
- Approach 2 is optimal in space complexity and shows deeper linked list manipulation skills.

### Script 
I'll first handle the simple solution by converting the linked list to an array.  
I traverse through the list, push all values into an array, then use two pointers to find twin sums.  
This gives me `O(n)` time and `O(n)` space.  
Now, for the optimal solution, I use fast and slow pointers to find the midpoint.  
Then I reverse the second half of the linked list in-place.
After that, I traverse from the head and from the reversed half simultaneously, computing twin sums and keeping track of the maximum.  
This solution is `O(n)` time and `O(1)` space.

