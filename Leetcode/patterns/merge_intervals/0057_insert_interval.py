# solution 1: brute force
# time: O(n log n)
# space: O(1) excluding output; O(n) if counting output list merged

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Brute force idea:
        - Append the new interval, sort by start, then run the LC56 merge template.
        Time: O(n log n) due to sorting
        Space: O(n) for the output list (aux O(1) excluding output)
        """
        if not intervals:
            return [newInterval]

        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        merged = []  # result after merging
        for s, e in intervals:
            if not merged or s > merged[-1][1]:
                merged.append([s, e])
            else:
                merged[-1][1] = max(merged[-1][1], e)
        return merged


# solution 2: merge interval
# time: O(n)
# space: O(1) excluding output; O(n) if counting output list merged

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Canonical O(n) scan using the 'left / overlap / right' partition.
        Time: O(n)
        Space: O(n) for the output list (aux O(1) excluding output)
        """
        res = []
        i, n = 0, len(intervals)
        new_s, new_e = newInterval

        # A) push all intervals that end before newInterval starts
        while i < n and intervals[i][1] < new_s:
            res.append(intervals[i])
            i += 1

        # B) merge everything that overlaps with [new_s, new_e]
        while i < n and intervals[i][0] <= new_e:
            new_s = min(new_s, intervals[i][0])
            new_e = max(new_e, intervals[i][1])
            i += 1
        res.append([new_s, new_e])  # the merged block

        # C) append the rest (all strictly to the right)
        while i < n:
            res.append(intervals[i])
            i += 1

        return res


# solution 3: bisect
# time: O(n)
# space: O(n) 

from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Advanced: boundary-finding via binary search on starts/ends.
        Steps:
        - Build two monotonic arrays: ends[], starts[] from intervals.
        - Find the overlap window [left:right) using bisect on ends/starts.
        - Merge newInterval with intervals[left:right], then assemble the result.
        Time: O(n) to build arrays + O(log n) bisects + O(n) for slicing → O(n)
        Space: O(n) for starts/ends/result (aux O(n))
        """
        if not intervals:
            return [newInterval]

        starts = [s for s, _ in intervals]
        ends   = [e for _, e in intervals]
        new_s, new_e = newInterval

        # Intervals strictly on the left: ends < new_s
        left = bisect_left(ends, new_s)
        # Intervals strictly on the right: starts > new_e
        right = bisect_right(starts, new_e)

        # If there is no overlap (left == right), we just insert between
        if left == right:
            return intervals[:left] + [[new_s, new_e]] + intervals[left:]

        # Merge overlapped block [left:right)
        merged_s = min(new_s, intervals[left][0])
        merged_e = max(new_e, intervals[right - 1][1])

        # Assemble result: left part + merged + right part
        return intervals[:left] + [[merged_s, merged_e]] + intervals[right:]
