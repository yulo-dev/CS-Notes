# Leetcode 0019 - Remove Nth Node From End of List

## ☀️ UMPIRE

- **Understand**: Given the head of a singly linked list, remove the **n-th node from the end** and return the head of the modified list.

- **Match**: This is a classic **Two Pointers** pattern, ideal for problems where you want to find the relative position of a node from the end.

- **Plan**:

  - Add a **dummy node** before the head to simplify edge case handling.
  - Use two pointers: `fast` and `slow`, both starting from the dummy.
  - Move `fast` `n` steps ahead to create a gap.
  - Move both pointers one step at a time until `fast.next` is null.
  - `slow.next` will be the node to remove. Skip it using `slow.next = slow.next.next`.
  - Return `dummy.next` as the new head.

- **Implement**: See code section below

- **Review**:

  - Don't forget to return `dummy.next` instead of `head`.
  - Use a dummy node to elegantly handle cases where the head is removed.

- **Evaluate**:

  - Time: O(L), where L is the length of the list
  - Space: O(1) constant space

---

## ☀️ Why This Is a Two Pointers Problem

We create a gap of `n` between `fast` and `slow` so that when `fast` reaches the end, `slow.next` points to the node we want to remove.

- Only one pass through the list
- Avoids computing list length manually
- Works even if the node to remove is the head

---

## ☀️ Edge Case Notes

| Input            | Description                      | Expected Output |
| ---------------- | -------------------------------- | --------------- |
| `[]`, n=1        | Empty list                       | `[]`            |
| `[1]`, n=1       | Single node, remove it           | `[]`            |
| `[1, 2]`, n=2    | Remove the head (first node)     | `[2]`           |
| `[1, 2, 3]`, n=3 | Remove the head of a longer list | `[2, 3]`        |
| `[1, 2, 3]`, n=1 | Remove the tail (last node)      | `[1, 2]`        |
| `[1, 2, 3]`, n=2 | Remove the middle node           | `[1, 3]`        |

These help you test:

- Head removal (check dummy handling)
- Tail removal (check `fast.next` logic)
- Proper n-gap pointer advancement

---

## ☀️ Code (Two Pointers)

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node that points to the head
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Move the fast pointer n steps ahead to create the gap
        for _ in range(n):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from end by skipping it
        slow.next = slow.next.next

        # Return the new head (might be different if we removed the first node)
        return dummy.next
```

---

## ☀️ Python Notes

- `dummy = ListNode(0, head)` helps in removing the head node easily
- `for _ in range(n):` moves `fast` ahead by `n` steps → gives us a `n`-step lead
- `while fast.next:` ensures that `slow` stops at the node just before the one to delete

---

## ☀️ Coding Walkthrough Script 

- First, I add a dummy node before the head to simplify cases where the head is removed.
- Then I move the fast pointer `n` steps forward to create a gap between fast and slow.
- Next, I move both fast and slow together until fast reaches the end of the list.
- At this point, slow is just before the node we want to remove.
- I remove it by doing `slow.next = slow.next.next`.
- Finally, I return `dummy.next` as the new head of the modified list.

---

## ☀️ Brute Force vs Two Pointers

| Method       | Time Complexity | Space Complexity | Notes                                |
| ------------ | --------------- | ---------------- | ------------------------------------ |
| Brute Force  | O(L) + O(L)     | O(1)             | Count total length, then re-traverse |
| Two Pointers | O(L)            | O(1)             | One-pass, cleaner with dummy node    |

---

## ☀️ Linked List Insights

- Linked Lists are great for **fast insertion/deletion** (O(1)) if you have the node reference.
- But they are **slow to access by index** — O(n) traversal needed from head.
- In **singly linked lists**, you can only move **forward**, not backward.
- In **doubly linked lists**, you can traverse both ways — but extra memory is needed.
- To find the length or reach the end, you must loop through manually — you cannot just use +1 like arrays. This is a key tradeoff in using Linked Lists.

---

## ☀️ Note on Range(n)

why we use `range(n)`:

I’m using `range(n)` here to advance the fast pointer exactly `n` steps forward, because `range(n)` will loop `n` times starting from 0. That gives me the gap I want between fast and slow.

or:

I want the fast pointer to be `n` steps ahead of slow, so I move fast forward using `range(n)` — this gives the correct offset even though the index starts at 0.

