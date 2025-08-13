# LeetCode 253 - Meeting Rooms II
# Three approaches for interviews: Brute Force -> Min-Heap -> Two Pointers

# solution 1: brute force (pairwise overlap counting)
# time: O(n^2)
# space: O(1)

from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Brute force framing (not recommended to implement in interviews, but useful to explain):
        - For each meeting i, count how many meetings overlap with it.
        - Track the maximum overlap across all i.
        Overlap rule (half-open [s, e)): two intervals [a,b) and [c,d) overlap iff a < d and c < b.
        Time: O(n^2) from pairwise checks.
        Space: O(1) extra.
        """
        n = len(intervals)
        if n == 0:
            return 0

        max_overlap = 0

        for i in range(n):
            s_i, e_i = intervals[i]
            overlap = 0
            for j in range(n):
                if i == j:
                    continue
                s_j, e_j = intervals[j]
                # Count an overlap if interval j intersects interval i
                if s_i < e_j and s_j < e_i:
                    overlap += 1
            # overlap counts "other" meetings overlapping i; include i itself (+1)
            max_overlap = max(max_overlap, overlap + 1)

        return max_overlap


# solution 2: Min-Heap by end time (straightforward & widely accepted)
# time: O(n log n)  (sorting + O(log n) per push/pop in the heap)
# space: O(n)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Min-heap by end time:
        - Sort meetings by start time.
        - Keep a min-heap of end times for ongoing meetings.
        - For each meeting (s, e):
            * If the earliest end time <= s, pop (a room frees up).
            * Push e (allocate/reuse a room for current meeting).
        - The heap size at the end equals the max concurrent meetings (rooms needed).
        Time: O(n log n), Space: O(n).
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])  # sort by start time

        heap: list[int] = []  # min-heap of end times

        for s, e in intervals:
            if heap and heap[0] <= s:
                heapq.heappop(heap)  # free the earliest room
            heapq.heappush(heap, e)    # occupy a room until 'e'

        return len(heap)


# solution 3: Two pointers on starts & ends (same asymptotics, smaller constant, very clean)
# time: O(n log n)  (sorting starts and ends)
# space: O(n)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Two-pointers sweep on starts & ends:
        - Extract & sort all start times and end times separately.
        - Use two pointers i (start) and j (end) to walk the timeline:
            * If starts[i] < ends[j], a meeting starts before any meeting frees → rooms += 1; i += 1
            * Else, a meeting frees (or ends exactly now) → rooms -= 1; j += 1
        - Track the maximum 'rooms' over time.
        Equality handling:
        - Using '<' (not '<=') ensures [s,e) semantics: if start == end, we free first then reuse.
        Time: O(n log n), Space: O(n).
        """
        n = len(intervals)
        if n == 0:
            return 0

        starts = [s for s, _ in intervals]
        ends   = [e for _, e in intervals]
        starts.sort()
        ends.sort()

        i = j = 0
        rooms = ans = 0

        while i < n:
            if starts[i] < ends[j]:
                rooms += 1
                ans = max(ans, rooms)
                i += 1
            else:
                rooms -= 1
                j += 1

        return ans
