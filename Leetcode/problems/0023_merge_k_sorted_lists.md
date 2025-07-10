# Leetcode 0023 - Merge k Sorted Lists

## ☀️ UMPIRE (Min Heap Method)
- **Understand**: Merge k sorted linked lists into one sorted linked list.
- **Match**: Input is multiple sorted lists → suitable for heap-based merging.
- **Plan**: Use a min heap to always extract the smallest head node from current candidates.
- **Implement**: See below (min heap approach with tuple `(val, index, node)`)
- **Review**: Ensure each popped node's `.next` is pushed back into the heap.
- **Evaluate**: Time O(n log k), where n = total nodes and k = number of lists. Space O(k) for the heap.

## ☀️ Metadata (Min Heap Method)
- **Appears In**: Grind75
- **Pattern**: Heap
- **Data Structure**: Linked List, Min Heap
- **Algorithm**: Greedy selection with heap
- **Tags**: Heap, Linked List, Priority Queue, Merge


## ☀️ Solution Code (Min Heap)

```python
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
```

## ☀️ Line-by-line Typing Script (Min Heap)

- Define the function `mergeKLists` that accepts a list of ListNode heads.
- Create a min heap to store the current smallest node from each list.
- Loop through all lists using `enumerate`, and push the first node of each list into the heap.
- Initialize a dummy ListNode and a pointer `current` to build the merged list.
- Enter the while-loop: while the heap is not empty:
  - Pop the smallest element (by val) from the heap.
  - Attach this node to the result list via `current.next`.
  - Move `current` forward to the node just added.
  - If the popped node has a `.next`, push it into the heap (so the list keeps participating).
- When done, return `dummy.next` (skipping the dummy head).
  

## ☀️ UMPIRE (Divide & Conquer Method)
- **Understand**: Merge k sorted linked lists into one sorted list by pairwise merging.
- **Match**: Multiple sorted sequences → merge sort pattern fits.
- **Plan**: Recursively split lists in half and merge them pairwise.
- **Implement**: See below (divide and conquer with `mergeTwoLists` helper).
- **Review**: Base case should return the list directly when only 1 or 0 list remains.
- **Evaluate**: Time O(n log k), Space O(log k) due to recursion.


## ☀️ Metadata (Divide & Conquer Method)
- **Appears In**: Grind75
- **Pattern**: Divide & Conquer
- **Data Structure**: Linked List
- **Algorithm**: Recursion, Merge Sort
- **Tags**: Recursion, Divide & Conquer, Linked List


## ☀️ Solution Code (Divide & Conquer)

```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2
        return dummy.next
```

## ☀️ Line-by-line Typing Script (Divide & Conquer)

- Define the `mergeKLists` function that takes a list of ListNode heads.
- Handle base cases: if the list is empty, return None; if it has one list, return that list.
- Split the input list into two halves: left and right.
- Recursively call `mergeKLists` on both halves.
- Merge the two resulting lists with `mergeTwoLists`.
- Inside `mergeTwoLists`, create a dummy node and pointer `tail`.
- While both `l1` and `l2` are non-empty, choose the smaller one and attach it to `tail.next`.
- Move `tail` forward and advance whichever list you took the node from.
- After the loop, attach the remaining part of `l1` or `l2` (whichever is not None) to `tail.next`.
- Return `dummy.next` which is the head of the merged list.

## ☀️ Complexity Table (Min Heap)

| Code Segment                                  | Operation         | Single Cost | Total Times | Total Cost       |
|----------------------------------------------|-------------------|-------------|-------------|------------------|
| `heapq.heappush(...)` (initial k heads)      | Push to heap      | O(log k)    | ≤ k       | O(k log k) ✔ (ignored) |
| `heapq.heappop(...)`                         | Pop smallest node | O(log k)    | n           | ✔ O(n log k)  |
| `heapq.heappush(...)` on `node.next`         | Push next node    | O(log k)    | ≤ n       | ✔ O(n log k)  |
| `current.next = node` and move pointer       | Pointer update    | O(1)        | n           | O(n) ✔ (minor)     |


## ☀️ Complexity Table (Divide & Conquer)

| Code Segment                    | Operation             | Single Cost | Total Times | Total Cost       |
|--------------------------------|------------------------|-------------|-------------|------------------|
| `mergeTwoLists()`              | Merge 2 lists          | O(m)        | log k layers | ✔ O(n log k)  |
| Recursion depth                | Call stack space       | -           | log k        | ✔ O(log k)    |
| `tail.next = l1 or l2`         | Tail connection        | O(1)        | n           | O(n) ✔ (minor)     |
