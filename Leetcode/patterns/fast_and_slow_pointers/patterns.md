
# Fast & Slow Pointers Patterns Summary

---

## Pattern 1: Detecting Cycle in Linked List (Floyd’s Algorithm)

### When to Use
- Detect if a linked list has a cycle.
- Find the starting point of the cycle.
- Find the length of the cycle.

### How to Recognize
- Problem explicitly mentions "cycle", "loop", "circular".
- Given a linked list head and asked to check for cycle or find cycle entry.

### Tips
- Use two pointers: `slow` moves one step, `fast` moves two steps.
- If `slow == fast` → cycle exists.
- For cycle entry: move one pointer to head, keep the other at meeting point, move both one step each until they meet.

### Template
```python
# check cycle + get the entry: 142 & 287

slow = fast = head

# step 1: check cycle
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    # if there's a cycle
    if slow == fast:
        # step 2: check entry
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

return None
```

### Problems
- 0142 Linked List Cycle II
- 0287 Find the Duplicate Number

---

## Pattern 2: Detecting Cycle in Array (Circular Movement)

### When to Use
- Detect if moving in an array forms a cycle.
- Movement uses values as steps, can wrap around.

### How to Recognize
- Problem talks about "circular array" or "wrap around".
- Movement index uses `(i + nums[i]) % n`.

### Tips
- Track direction consistency (all positive or all negative).
- Avoid single-element cycles.
- Mark visited nodes as 0 to avoid reprocessing.

### Template
```python
def circularArrayLoop(nums):
    def next_index(i):
        return (i + nums[i]) % len(nums)

    for i in range(len(nums)):
        if nums[i] == 0: 
            continue
        direction = nums[i] > 0
        slow = fast = i
        while True:
            if (nums[slow] > 0) != direction: break
            slow = next_index(slow)
            if (nums[slow] > 0) != direction: break
            fast = next_index(fast)
            if (nums[fast] > 0) != direction: break
            fast = next_index(fast)
            if (nums[fast] > 0) != direction: break
            if slow == fast:
                if slow == next_index(slow): break
                return True
        # mark visited
        marker = i
        while nums[marker] != 0 and (nums[marker] > 0) == direction:
            next_pos = next_index(marker)
            nums[marker] = 0
            marker = next_pos
    return False
```

### Problems
- 0457 Circular Array Loop

---

## Pattern 3: Palindrome Linked List & Maximum Twin Sum

### When to Use
- Need to check if a linked list is a palindrome.
- Need to find the maximum twin sum in a linked list.
- Need to find the middle node for splitting/reversing.

### How to Recognize
- Problem asks about comparing first and second half.
- Often requires reversing the second half.

### Tips
- Use fast/slow to find middle.
- Reverse second half and compare values.
- Restore list if required by problem.

### Template
```python
# check cycle + reverse linkedlist + check palindrome or check max sum: 234, 2130

slow = fast = head

# step 1: find middle
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

# step 2: reverse linkedlist
prev = None
while slow:
    nxt = slow.next
    slow.next = prev
    prev = slow
    slow = nxt

# step 3: do the checking
left = head
right = prev
while right:
    # do some checking rules
    left = left.next
    right = right.next

return xxx
```

### Problems
- 0234 Palindrome Linked List
- 2130 Maximum Twin Sum of a Linked List
- 0876 Middle of the Linked List

---

## Pattern 4: Split Circular Linked List

### When to Use
- Given a circular linked list, split it into two halves.

### How to Recognize
- Problem explicitly says "circular linked list".
- Usually requires identifying the midpoint.

### Tips
- Use slow/fast to find midpoint.
- Handle circular pointers carefully to avoid infinite loop.

### Template
```python
def splitCircularList(head):
    slow = fast = head
    while fast.next != head and fast.next.next != head:
        fast = fast.next.next
        slow = slow.next
    head1 = head
    head2 = slow.next
    slow.next = head1
    if fast.next.next == head:
        fast = fast.next
    fast.next = head2
    return head1, head2
```

### Problems
- 2674 Split a Circular Linked List
