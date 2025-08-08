# Leetcode 187 — Repeated DNA Sequences

## ☀️ Problem Summary
Find all 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

---

## ☀️ Tags
- Hashing
- Sliding Window
- String
- Bit Manipulation (Advanced)

---

## ☀️ Data Structure
- **Set**: for fast O(1) lookup of seen substrings
- **Integer (bitmask)** in advanced version for rolling hash encoding

---

## ☀️ Algorithm
### Brute Force
Check every possible substring and count occurrences by scanning the whole string.

### Sliding Window + Sets
Slide a fixed-length window of size 10, record seen substrings, and collect duplicates.

### Bit Encoding + Rolling Hash
Encode A/C/G/T into 2 bits, maintain a rolling hash for O(1) substring transition.

---

## ☀️ Complexity Analysis

| Version | Time Complexity | Space Complexity | Notes |
|---------|-----------------|------------------|-------|
| Brute Force | O(n²·L) (≈ O(n²) since L=10) | O(1) | Two nested loops for all substrings |
| Sliding Window + Set | O(n·L) → O(n) for L=10 | O(n) | Set lookup O(1) |
| Bit Encoding + Rolling Hash | O(n) | O(n) | Lower constant factor, avoids slicing |

---

## ☀️ Solutions

### Version A — Brute Force
```python
from typing import List

class SolutionBF:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        n = len(s)
        if n < L:
            return []
        res: List[str] = []

        for i in range(n - L + 1):
            sub = s[i:i+L]
            cnt = 0
            for j in range(n - L + 1):
                if s[j:j+L] == sub:
                    cnt += 1
            if cnt > 1 and sub not in res:
                res.append(sub)

        return res
```

---

### Version B — Sliding Window + Sets
```python
from typing import List

class SolutionSW:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        n = len(s)
        if n < L:
            return []

        seen = set()
        dups = set()

        for i in range(n - L + 1):
            sub = s[i:i+L]
            if sub in seen:
                dups.add(sub)
            else:
                seen.add(sub)

        return list(dups)
```

---

### Version C — Bit Encoding + Rolling Hash
```python
from typing import List

class SolutionBit:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        n = len(s)
        if n < L:
            return []

        code = {'A':0, 'C':1, 'G':2, 'T':3}
        mask = (1 << (2 * L)) - 1

        seen_hashes = set()
        dups = set()
        h = 0

        for i in range(L):
            h = (h << 2) | code[s[i]]
        seen_hashes.add(h)

        for i in range(L, n):
            h = ((h << 2) | code[s[i]]) & mask
            if h in seen_hashes:
                dups.add(s[i - L + 1 : i + 1])
            else:
                seen_hashes.add(h)

        return list(dups)
```

---

## ☀️ Script
We need to find all DNA sequences of length 10 that appear more than once.
I'll use a sliding window of length 10.
Maintain a `seen` set for sequences we've encountered, and a `repeated` set for sequences we find again.
At the end, return the repeated sequences as a list.
