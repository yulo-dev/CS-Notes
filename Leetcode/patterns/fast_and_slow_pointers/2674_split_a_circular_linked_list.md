
# LeetCode 2674 – Split a Circular Linked List

## ☀️ Problem Summary
Given a circular singly-linked list, split it into two circular linked lists:
- The **first half** should have `ceil(n/2)` nodes.
- The **second half** should have the remaining nodes.
- Return the two heads of these new circular linked lists.

---

## ☀️ UMPIRE

### **Understand**
- Input: Circular linked list `head`.
- Output: `[head1, head2]` – heads of two circular linked lists.
- Edge cases:
  - `head = None`
  - Single node: return `[head, None]`.

### **Match**
- We need to find the **midpoint** of the list and **split** it.
- Circular nature means there is no `None` end marker → special stop condition.
- Common approach: **Fast & Slow Pointers**.

### **Plan**
1. Use **slow** and **fast** pointers to find midpoint:
   - `slow` moves one step.
   - `fast` moves two steps.
   - Stop when `fast.next == head` or `fast.next.next == head`.
2. For odd-length lists, move `fast` one step to reach actual tail.
3. `second = slow.next` → head of second half.
4. Close both halves:
   - `fast.next = second` (close second half)
   - `slow.next = head` (close first half)
5. Return `[head, second]`.

### **Implement (Optimized One-Pass Version)**
```python
def splitCircularLinkedList(head):
    if not head or head.next == head:
        return [head, None]

    slow = fast = head

    # Find midpoint
    while fast.next != head and fast.next.next != head:
        slow = slow.next
        fast = fast.next.next

    # Adjust fast for odd length lists
    if fast.next != head:
        fast = fast.next

    second = slow.next
    fast.next = second
    slow.next = head

    return [head, second]
```

### **Review**
- Handles even and odd lengths correctly.
- Time Complexity: **O(n)** (one pass).
- Space Complexity: **O(1)**.

### **Evaluate**
- Works for edge cases.
- Uses minimal pointer updates.

---

## ☀️ Why Fast & Slow Pointers?
- We need to find the midpoint efficiently in **one pass**.
- Slow moves one step, fast moves two steps:
  - When fast reaches the end (or loops back in circular lists), slow is at midpoint.
- Prevents converting the list into an array or doing multiple passes.

---

## ☀️ Insights Noticed During Solving
1. **Two-Pass Version Exists:**  
   - Some implementations cut the first half, then iterate again to find the second half tail.  
   - This is safe but redundant.
2. **Tail Handling Difference (Circular vs Normal Lists):**  
   - In normal lists, loop condition is `while fast and fast.next:`.  
   - In circular lists, we stop early: `while fast.next != head and fast.next.next != head:`.  
   - This may cause `fast` to stop one node before the true tail in odd lengths → we add one step (`fast = fast.next`) to fix it.
3. **Returning Heads Works Naturally:**  
   - Linked lists are pointer-based; returning the `second` pointer is enough to represent the new circular list.

---

## ☀️ Script 
We can solve this in O(n) time and O(1) space.  
First, I use slow and fast pointers to find the midpoint.  
Because the list is circular, we check `fast.next != head and fast.next.next != head` to avoid infinite loops.  
After finding midpoint, we move fast one more step in odd-length lists to reach the true tail.  
Then we split: `second = slow.next`, make `fast.next = second` (closing the second half) and `slow.next = head` (closing the first half).  
This yields two circular linked lists with correct node counts.
