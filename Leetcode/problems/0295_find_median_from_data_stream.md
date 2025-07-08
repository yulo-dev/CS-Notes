# Leetcode 0295 - Find Median from Data Stream

## ☀️ UMPIRE

- **Understand**: Design a data structure that supports adding numbers and finding the median at any point. Median is the middle value in a sorted list (average of two middles if even).
- **Match**: Input is a data stream → suitable for heaps to maintain ordered halves.
- **Plan**: Use two heaps: max heap for lower half (store negative values), min heap for upper half. Always insert into max heap first, then rebalance.
- **Implement**: See below
- **Review**: Verify balance condition (size difference ≤ 1), and that max(left) ≤ min(right)
- **Evaluate**: Time: O(log n) per add, O(1) per find. Space: O(n) for storing all numbers in heaps
- n refers to the number of elements that have been added to the data stream so far — the total count of addNum() calls. 

## ☀️ Metadata

- **Appears In**: Grind75
- **Pattern**: Heap + Two Heaps
- **Data Structure**: Heap (min heap, max heap)
- **Algorithm**: Insertion + Heap balancing
- **Tags**: Heap, Priority Queue, Data Stream, Design

## ☀️ Solution Code

```python
import heapq

class MedianFinder:

    def __init__(self):
        # Max heap (as negatives) to store the smaller half of numbers
        self.left = []   # max heap = negative values
        # Min heap to store the larger half of numbers
        self.right = []  # min heap = normal values

    def addNum(self, num: int) -> None:
        # Step 1: Always push to max heap (store as negative to simulate max heap)
        heapq.heappush(self.left, -num)

        # Step 2: Make sure every element in left <= every element in right
        if self.left and self.right and (-self.left[0] > self.right[0]):
            # Move the max from left to right
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        # Step 3: Balance the lengths (allow only a max difference of 1)
        if len(self.left) > len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        elif len(self.right) > len(self.left):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)

    def findMedian(self) -> float:
        # If odd total, the extra number is in max heap (left)
        if len(self.left) > len(self.right):
            return -self.left[0]
        # If even total, average the two middle values
        else:
            return (-self.left[0] + self.right[0]) / 2.0
```

## ☀️ Line-by-line Typing Script

- I’m importing the heapq module to use heap operations in Python.
- I define a class called MedianFinder to maintain a running median.
- In the constructor, I create two lists:
  - `self.left` will be a max heap using negative values.
  - `self.right` will be a regular min heap.
- In `addNum`, I start by always pushing the number to the left heap, as a negative value.
- Then I check whether the max from the left is greater than the min from the right.
- If so, I pop from the left and push to the right to restore order.
- Next, I balance the heaps to ensure their size difference is no more than 1.
- If left has more than one extra, pop from left and push to right.
- If right is longer, pop from right and push to left (as negative).
- For `findMedian`, if left is longer, the median is the top of left (convert back to positive).
- If they are equal in size, the median is the average of the tops of both heaps.
