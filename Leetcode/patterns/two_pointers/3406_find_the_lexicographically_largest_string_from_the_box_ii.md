# Leetcode 3406 - Find the Lexicographically Largest String From the Box II

## ☀️ UMPIRE

### Understand

We are given a string `word` and an integer `numFriends`. In the game, `word` is split into `numFriends` non-empty strings in all possible unique ways. Each split generates several substrings, all of which are collected into a box. We need to return the **lexicographically largest** string from that box.

**Key Observations:**

1. Every unique split is considered, so many substrings are generated.
2. The maximum length of a single substring in any one split is `len(word) - numFriends + 1`.
3. To maximize lexicographic order, we should focus on substrings starting with the lexicographically largest character.
4. If `numFriends == 1`, no splitting is allowed, so the entire string is taken.

### Match

- Pattern: **String Processing + Greedy**
- Focus: **Lexicographical comparison** of substrings.
- Not a Two Pointers problem (no dynamic left/right movement).

### Plan (Optimized)

1. If `numFriends == 1`, simply return the entire word.
2. Calculate `maxLength = len(word) - numFriends + 1`.
3. Find the maximum character `max_char` in the string.
4. Iterate through each index `i` where `word[i] == max_char`, slice the substring of length `maxLength`.
5. Compare with the current best substring and update if greater.
6. Return the best substring.

### Implement (Optimized)

```python
class Solution:
    def findLexicographicallyLargestString(self, word: str, numFriends: int) -> str:
        n = len(word)

        # Special case: only one segment allowed -> return whole word
        if numFriends == 1:
            return word

        # Max allowed substring length from one segment
        maxLength = n - numFriends + 1

        # Find lexicographically largest character
        max_char = max(word)

        best = ""
        for i, ch in enumerate(word):
            if ch == max_char:
                candidate = word[i:i + maxLength]
                if candidate > best:
                    best = candidate
        return best
```

### Brute Force Approach

**Idea:** Enumerate **all possible splits** of `word` into `numFriends` non-empty parts. Collect all substrings generated in each split, then pick the lexicographically largest.

**Pseudocode:**

```python
# Generate all combinations of (numFriends-1) cut positions
for each combination of cut positions:
    split_word = split the word according to cuts
    for each substring in split_word:
        add to box
return max(box)
```

**Complexity:**

- Generating all splits: O(C(n-1, numFriends-1))
- Collecting and comparing substrings: Potentially exponential for large n.
- This is not feasible for n up to 2 \* 10^5.

### Review

- **Edge Case:** If `numFriends == 1`, must return the whole string (previous wrong output was just picking the largest suffix).
- **Correctness:** Focuses only on substrings starting with `max_char`, reducing unnecessary comparisons.
- **Python slicing safety:** `word[i:i+maxLength]` is safe even if it exceeds the string length.

### Evaluate

- **Optimized Time Complexity:** O(n)
- **Optimized Space Complexity:** O(1) (ignoring output string)
- **Brute Force Time Complexity:** Exponential in worst case, not feasible.

## ☀️ Metadata

- **Tags:** String, Greedy, Lexicographical Order
- **Data Structure:** String
- **Algorithm:** Greedy substring search

## ☀️ Example Walkthrough

### Example 1:

```
word = "dbca", numFriends = 2
```

- maxLength = 4 - 2 + 1 = 3
- max\_char = 'd'
- Candidates starting with 'd': "dbc"
- Output = "dbc"

### Example 2:

```
word = "ahl", numFriends = 1
```

- numFriends == 1 -> return whole string = "ahl"

## ☀️ Script

We need the lexicographically largest string from all possible splits. A brute force solution would try every split, collect all substrings, and then find the max, which is exponential and infeasible. Instead, we observe that we only need to consider substrings starting with the maximum character and of length at least n - numFriends + 1. If numFriends equals 1, we simply return the whole word. The optimized approach runs in O(n) time and O(1) space.

