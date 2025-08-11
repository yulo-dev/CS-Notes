# solution 1: Brute Force
# time: O(m * n) 
# space: O(1) 

from typing import List

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        Brute force with early breaks.
        For each interval in A, scan B and prune using sorted order:
        - if B[j].end < A[i].start: keep scanning (no chance to intersect yet)
        - if B[j].start > A[i].end: break (future B's start even larger)
        Time:  O(m * n) in the worst case
        Space: O(1) extra (excluding the output list)
        """
        res: List[List[int]] = []

        for a_start, a_end in A:
            for b_start, b_end in B:
                # If B ends before A starts => cannot intersect; keep looking
                if b_end < a_start:
                    continue
                # If B starts after A ends => no later B can intersect A; stop inner loop
                if b_start > a_end:
                    break

                # Compute intersection candidate for closed intervals
                start = max(a_start, b_start)
                end   = min(a_end, b_end)
                if start <= end:
                    res.append([start, end])

        return res





# solution 2: Simplified pointer move
# time: O(m + n) 
# space: O(1) 

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        Two-pointer scan with precise advancement:
        - Move the pointer whose interval ends first.
        - If both intervals end at the same position, move both pointers.
        This avoids an extra comparison in the next iteration when ends tie.
        Time:  O(m + n)
        Space: O(1) extra (excluding the output list)
        """
        i = j = 0
        res = []

        while i < len(firstList) and j < len(secondList):
            a1, a2 = firstList[i]
            b1, b2 = secondList[j]

            # Compute the potential intersection [start, end]
            start = max(a1, b1)
            end = min(a2, b2)

            # Because intervals are CLOSED, start == end is a valid point intersection
            if start <= end:
                res.append([start, end])

            # Move the pointer(s) that have been "consumed" on the right boundary.
            # If both end together, advance both to avoid an extra (useless) comparison.
            if a2 < b2:
                i += 1
            elif a2 > b2:
                j += 1
            else:
                i += 1
                j += 1

        return res
