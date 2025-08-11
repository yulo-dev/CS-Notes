# solution 1: brute force

from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
        Brute-force check: for each interval i, see if there exists
        another interval j that covers it.
        Interval A = [a1, a2] is covered by B = [b1, b2] iff b1 <= a1 and a2 <= b2.
        Because these are CLOSED intervals, equality on the ends counts as coverage.

        Time:  O(n^2)   -- for each i, we may scan all j
        Space: O(1)     -- extra (excluding input)
        """
        n = len(intervals)
        uncovered = 0

        for i in range(n):
            s_i, e_i = intervals[i]
            covered = False

            # Look for ANY j != i that covers [s_i, e_i]
            for j in range(n):
                if i == j:
                    continue
                s_j, e_j = intervals[j]
                # Coverage condition for closed intervals (<= on both comparisons)
                if s_j <= s_i and e_i <= e_j:
                    covered = True
                    break

            if not covered:
                uncovered += 1

        return uncovered



# solution 2: Advanced (Sort by start asc, end desc + One Pass, O(n log n))
from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
        Optimal approach:
        1) Sort by (start asc, end desc) so longer intervals with the same start
           come first (potential "cover-ers" appear before "cover-ees").
        2) Scan once, keeping the rightmost end (max_end) we've seen:
           - If current end <= max_end  → current is covered (skip it).
           - Else                       → current is not covered (count it), update max_end.

        Why end DESC on tie?
        - For intervals like [1,4] and [1,3], we want [1,4] to appear first.
          Then when we meet [1,3], its end (3) <= max_end (4) → covered.

        Time:  O(n log n) for sorting + O(n) scan
        Space: O(1) extra (excluding input)
        """
        # Crucial tie-break: end DESC so longer intervals come first when starts are equal
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        max_end = float('-inf')

        for s, e in intervals:
            # If current end extends beyond max_end, it cannot be covered by any previous
            if e > max_end:
                count += 1
                max_end = e
            # else: e <= max_end → covered → do nothing

        return count
