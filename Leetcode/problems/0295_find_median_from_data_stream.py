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
