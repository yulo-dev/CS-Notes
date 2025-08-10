# solution 1: brute force
# time: O(n²) 
# space: O(1)

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Brute force idea:
        - Keep merging any overlapping pair in repeated passes
          until no more merges happen.
        - Each pass scans all pairs; when we merge one pair,
          we restart another pass.
        Time: worst-case can be O(n^2) ~ O(n^3) due to repeated scans and deletions.
        Space: O(1) extra (ignoring sorting if you sort).
        """
        if not intervals:
            return []

        # (Optional) sort first to make finding overlaps easier (not required for brute force,
        # but it helps reduce random pair checks and makes behavior more predictable).
        intervals.sort(key=lambda x: x[0])

        changed = True
        while changed:
            changed = False
            n = len(intervals)
            i = 0
            while i < n:
                j = i + 1
                while j < n:
                    a_start, a_end = intervals[i]
                    b_start, b_end = intervals[j]

                    # Overlap condition (touching counts as overlap in LC56):
                    if not (b_start > a_end or a_start > b_end):
                        # Merge i and j into a single interval [min_start, max_end]
                        merged = [min(a_start, b_start), max(a_end, b_end)]
                        # Replace i with merged, remove j
                        intervals[i] = merged
                        intervals.pop(j)
                        n -= 1
                        changed = True
                        # After modifying the list, restart inner scan from i+1
                        # (do not increment j here because we just popped it)
                    else:
                        j += 1
                i += 1

        return intervals


# solution 2: Merge Intervals (sort + single pass)
# time: O(nlogn) 
# space: O(n)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge Intervals - Canonical Solution
        Approach:
        1) Sort intervals by their start time.
        2) Iterate through each interval:
            - If the merged list is empty OR the current start is greater than 
              the last merged end → start a new interval.
            - Otherwise, they overlap → extend the end of the last merged interval.
        Time Complexity: O(n log n) due to sorting + O(n) scan.
        Space Complexity: O(n) for the output list.
        """
        # Edge case: no intervals (not needed for LC56 due to constraints, but kept for robustness)
        if not intervals:
            return []

        # Step 1: Sort by start time (index 0)
        intervals.sort(key=lambda x: x[0])

        merged = []  # Result list to hold merged intervals

        # Step 2: Iterate over intervals
        for start, end in intervals:
            # Case 1: No merged intervals yet, or no overlap with the last merged one
            if not merged or start > merged[-1][1]:
                merged.append([start, end])  # Create a new merged interval
            else:
                # Case 2: Overlap exists → extend the last merged interval's end
                merged[-1][1] = max(merged[-1][1], end)

        return merged


# solution 3:  In-place write-index (low extra space, same logic
# time: O(nlogn) 
# space: O(1)

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Advanced variant: in-place write index.
        - Still sort by start.
        - Use a 'write' pointer to overwrite the input array with merged intervals.
        Time: O(n log n) for sort + O(n) scan.
        Space: O(1) extra (besides sorting), since we reuse 'intervals'.
        """
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        write = 0  # number of merged intervals written so far, also next write position
        for i in range(len(intervals)):
            if write == 0 or intervals[i][0] > intervals[write - 1][1]:
                # No overlap -> write a new block at position 'write'
                intervals[write] = intervals[i]
                write += 1
            else:
                # Overlap -> extend the end in the last written block
                intervals[write - 1][1] = max(intervals[write - 1][1], intervals[i][1])

        # The merged result is the prefix [0:write]
        return intervals[:write]
