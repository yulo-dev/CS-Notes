# solution 1: Brute Force
# time: O(n²·L)（L=10 ⇒ O(n²))
# Space: O(1)

from typing import List

class SolutionBF:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        Brute force: for each length-10 substring, count its occurrences
        by scanning all positions; deduplicate in the result.
        """
        L = 10
        n = len(s)
        if n < L:
            return []
        res: List[str] = []

        for i in range(n - L + 1):
            sub = s[i:i+L]
            cnt = 0
            # Count occurrences of sub
            for j in range(n - L + 1):
                if s[j:j+L] == sub:
                    cnt += 1
            # Add once if it appears more than once
            if cnt > 1 and sub not in res:
                res.append(sub)

        return res


# solution 2: Sliding Window + Sets
# time: O(n·L)（L=10 ⇒ O(n))
# Space: O(n)

from typing import List

class SolutionSW:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        Fixed-length sliding window (L=10).
        - seen: substrings seen once
        - dups: substrings seen >= 2 (answers)
        """
        L = 10
        n = len(s)
        if n < L:
            return []

        seen = set()
        dups = set()

        # Slide window by 1; each slice is exactly L chars
        for i in range(n - L + 1):
            sub = s[i:i+L]                  # O(L) slice; with L=10 it's effectively constant
            if sub in seen:
                dups.add(sub)               # seen before -> it's a duplicate
            else:
                seen.add(sub)               # first time we see this substring

        return list(dups)



# solution 3: bit Encoding + Rolling Window
# time: O(n)
# Space: O(n)

from typing import List

class SolutionBit:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        Encode A/C/G/T into 2 bits and maintain a rolling 20-bit window.
        Using integers as keys reduces slicing and memory overhead.
        """
        L = 10
        n = len(s)
        if n < L:
            return []

        code = {'A':0, 'C':1, 'G':2, 'T':3}
        mask = (1 << (2 * L)) - 1     # keep lowest 2*L bits

        seen_hashes = set()           # hashes seen once
        dups = set()                  # final substrings (deduplicated)
        h = 0

        # Build the first window's hash
        for i in range(L):
            h = (h << 2) | code[s[i]]
        seen_hashes.add(h)

        # Roll the window across the string
        for i in range(L, n):
            h = ((h << 2) | code[s[i]]) & mask   # drop oldest 2 bits, add new 2 bits
            if h in seen_hashes:
                dups.add(s[i - L + 1 : i + 1])   # exact substring (no collisions with 2-bit DNA)
            else:
                seen_hashes.add(h)

        return list(dups)
