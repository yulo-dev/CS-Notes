# solution 1: Explicit merge, then subtract
# time: O(n log n)
# space: O(1)

from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        """
        Explicitly merge meetings (like LC56), then subtract union length from the total days.
        Closed intervals => length([s, e]) = e - s + 1
        Adjacent segments should be merged (e.g., [1,3] and [4,5]) since there's no free day between them.
        Time:  O(n log n) for sorting + O(n) merge pass
        Space: O(1) auxiliary (excluding the merged list as output-like temp)
        """
        if not meetings:
            # No meetings at all => all days are free
            return days

        # 1) Sort by start time
        meetings.sort(key=lambda it: it[0])

        # 2) Merge overlapping or adjacent intervals into 'merged'
        merged: List[List[int]] = []
        cur_s, cur_e = meetings[0]

        for s, e in meetings[1:]:
            # Overlap or adjacency on CLOSED intervals:
            # If the next start is <= current end + 1, there's no free gap; we extend.
            if s <= cur_e + 1:
                cur_e = max(cur_e, e)
            else:
                # Current block ends; push and start a new block
                merged.append([cur_s, cur_e])
                cur_s, cur_e = s, e

        # Don't forget the last block
        merged.append([cur_s, cur_e])

        # 3) Total covered length = sum of lengths of merged blocks
        covered = 0
        for s, e in merged:
            covered += (e - s + 1)  # closed interval length

        # 4) Free days = total days - covered days
        free_days = days - covered
        # Guard: free days cannot be negative (only if inputs exceed [1..days], but problem usually keeps within bounds)
        return max(0, free_days)


      
# solution 2: Implicit merge; single pass counting gaps
# time: O(n log n)
# space: O(1)

from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        """
        Implicitly merge by tracking 'prev_end' and summing gaps directly.
        Each gap between disjoint covered segments contributes (s - prev_end - 1).
        Closed intervals => adjacency (s == prev_end + 1) yields zero gap.
        Time:  O(n log n) for sorting + O(n) scan (or O(n) total if already sorted)
        Space: O(1) auxiliary
        """
        if not meetings:
            return days

        # Sort by start time to scan in chronological order
        meetings.sort(key=lambda it: it[0])

        free = 0
        prev_end = 0  # coverage so far: the rightmost day already covered by meetings

        for s, e in meetings:
            # If the next covered block starts strictly after 'prev_end',
            # the free gap is (prev_end+1 .. s-1) => length = s - prev_end - 1.
            if s > prev_end:
                free += max(0, s - prev_end - 1)
            # Extend the covered suffix to the farthest right end seen so far
            prev_end = max(prev_end, e)

        # Tail gap after the last covered day through 'days'
        free += max(0, days - prev_end)
        return free
