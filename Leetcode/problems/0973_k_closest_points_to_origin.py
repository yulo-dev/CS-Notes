import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Initialize an empty list to use as a max-heap
        max_heap = []

        # Iterate over each point in the input
        for x, y in points:
            # Compute squared distance from the origin (we use squared to avoid sqrt)
            dist = -(x * x + y * y)  # Use negative distance to simulate max-heap

            # Push the tuple (-distance, x, y) into the heap
            heapq.heappush(max_heap, (dist, x, y))

            # If the heap size exceeds k, remove the farthest point (which is on top)
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # Extract the k closest points from the heap and return them as a list of [x, y]
        return [[x, y] for (_, x, y) in max_heap]
