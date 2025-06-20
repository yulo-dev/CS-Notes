# ☀️ Leetcode 17 — Letter Combinations of a Phone Number

### ☀️ Problem
Given a string containing digits from 2–9, return all possible letter combinations that the number could represent. The mapping is the same as on a telephone button pad.


### ☀️ UMPIRE

**U — Understand**
- Input: digits (a string of digits from 2–9)
- Output: List of all possible letter combinations
- Constraints:
  - Only digits 2–9
  - Return empty list if input is ""

**M — Match**
- Backtracking
- Combinatorics

**P — Plan**
Use backtracking:
```python
def backtrack(index, path):
    if index == len(digits):
        res.append(path)
        return
    for letter in phone[digits[index]]:
        backtrack(index + 1, path + letter)
```

**R — Review**

- Time Complexity: O(4^n * n)
- Space Complexity: O(4^n * n) (from result list) + O(n) recursion stack (minor)

**E — Evaluate**
- Input: "23"
- Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


### ☀️ Code with Comments

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        if not digits:
            return []

        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        def backtrack(index, path):
            # Base case: full combination formed
            if index == len(digits):
                res.append(path)
                return

            # Try each letter mapped to the current digit
            for letter in phone[digits[index]]:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return res
```

### ☀️ Tags

- Backtracking
- DFS
- Recursion
- Mapping
- Strings

---

## ☀️ Trace

```
Input: [1, 2]

Call: backtrack(0, [])
→ res = [[]]

↳ i = 0 → path.append(1)
Call: backtrack(1, [1])
→ res = [[], [1]]

    ↳ i = 1 → path.append(2)
    Call: backtrack(2, [1, 2])
    → res = [[], [1], [1, 2]]

    ↳ path.pop() → path = [1]
↳ path.pop() → path = []

↳ i = 1 → path.append(2)
Call: backtrack(2, [2])
→ res = [[], [1], [1, 2], [2]]

↳ path.pop() → path = []

...
```

## ☀️ Line-by-line Script

- I'm defining a function called subsets that takes in a list of integers called nums and returns all its possible subsets.
- I create an empty list res to store all the subset combinations.
- Inside the function, I define a helper function backtrack, which takes the current index start and a list path that represents the current subset being built.
- At the beginning of each recursive call, I append a copy of path into res to record the current subset.
- Then, I start a for-loop from index start to the end of the list.
- For each number in this loop, I first add it to path.
- I recursively call backtrack again, but this time starting from the next index i + 1, so we don’t reuse the same number.
- After that recursive call finishes, I remove the last number from path using .pop() to backtrack and explore other combinations.
- Finally, I call backtrack(0, []) to start the process, and return res which now holds all the subsets.
