# solution 1: Brute-Force Range Fill (location-by-location simulation)
# time: O(n * L), where L <= 1000 (treated as O(1) here); slowest
# space: O(L)

from typing import List
import heapq

class SolutionBruteRange:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        Simulate passenger counts at each location (0..1000).
        For each trip [p, s, e) (half-open), add p to every point in [s, e-1].
        If any location exceeds capacity, return False; otherwise True.

        Time:  O(n * L), where L is the location range (<= 1000 in this problem)
        Space: O(L)
        """
        car = [0] * 1001  # passenger counts at each location

        for p, s, e in trips:
            # Early rejection: one trip alone exceeds capacity
            if p > capacity:
                return False
            # Fill the range [s, e) one by one
            for x in range(s, e):
                car[x] += p
                if car[x] > capacity:
                    return False

        return True


# solution 2: Min-Heap by end
# time: O(n log n)
# space: O(n)

class SolutionHeap:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        Min-heap by 'end' (general & intuitive):
        - Sort trips by start s.
        - Keep a min-heap of ongoing trips keyed by end position: (end, passengers).
        - Before picking up at s, pop all trips with end <= s (they've gotten off because trips are [s, e)).
        - Then pick up current trip; if current passengers exceed capacity → False.

        Time:  O(n log n) due to heap operations
        Space: O(n) for the heap
        """
        # Sort by start position
        trips.sort(key=lambda x: x[1])  # x = [p, s, e]

        heap: List[tuple[int, int]] = []  # (end, passengers)
        curr = 0  # current passengers in the car

        for p, s, e in trips:
            # Drop off all passengers whose trip already ended at or before s
            # Because intervals are half-open [s, e), end == s means they've already gotten off.
            while heap and heap[0][0] <= s:
                end, pp = heapq.heappop(heap)
                curr -= pp

            # Pick up current trip
            curr += p
            if curr > capacity:
                return False

            # Schedule their drop-off
            heapq.heappush(heap, (e, p))

        return True


# solution 3: Difference Array + Prefix Sum (recommend)
# time: O(n + L), where L <= 1000 (treated as O(1) here); fastest in this problem
# space: O(L), where L <= 1000 (treated as O(1) here)

class SolutionDiffArray:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        Difference array over location axis [0..1000]:
        For each trip [p, s, e) (half-open):
            diff[s] += p   # pick up at s
            diff[e] -= p   # drop off at e (at e they are already off)
        Then prefix-sum the diff; if any cumulative count > capacity → False.

        Time:  O(n + L), where L <= 1000 (treated as O(1) here)
        Space: O(L) for the diff array
        """
        # Problem guarantees 0 <= s < e <= 1000
        diff = [0] * 1001  # indices 0..1000 inclusive

        for p, s, e in trips:
            # Quick prune: a single trip exceeding capacity is impossible to carry
            if p > capacity:
                return False
            diff[s] += p
            diff[e] -= p  # half-open → at e they are off

        curr = 0
        for x in range(1001):
            curr += diff[x]  # prefix sum gives current passengers at position x
            if curr > capacity:
                return False

        return True
