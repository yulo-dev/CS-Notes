# Sliding Window Pattern Summary

---

## Pattern 1: Fixed-Size Sliding Window

### When to Use
- When the window size is fixed (e.g., length `k`).
- Need to process every contiguous subarray/substring of length `k`.

### How to Recognize
- Problem explicitly gives a fixed window length.
- Common in average, sum, or count calculations over a fixed range.

### Tips
- Maintain running sum/count to avoid recomputing from scratch.
- Add the new element, remove the element that falls out of the window.

### Template
```python
window_sum = sum(arr[:k])
max_sum = window_sum

for right in range(k, len(arr)):
    window_sum += arr[right] - arr[right - k]
    max_sum = max(max_sum, window_sum)
```

### Problems
- 0643 Maximum Average Subarray I
- 1456 Maximum Number of Vowels in a Substring of Given Length

---

## Pattern 2: Variable-Size Sliding Window (Shrink When Invalid)

### When to Use
- Window size not fixed, grows until a constraint is violated.
- Need to find the smallest/largest subarray meeting a condition.

### How to Recognize
- Problem states “at most/at least k condition”.
- Requires expanding and shrinking window dynamically.

### Tips
- Expand `right` pointer until condition breaks.
- Shrink `left` pointer until condition is satisfied again.

### Template
```python
left = 0
for right in range(len(arr)):
    # expand window
    while condition_not_satisfied:
        # shrink window
        left += 1
```

### Problems
- 0209 Minimum Size Subarray Sum
- 0424 Longest Repeating Character Replacement

---

## Pattern 3: Longest Substring with At Most K Distinct Characters

### When to Use
- Find the longest substring with up to `k` unique characters.

### How to Recognize
- Problem mentions “at most k distinct” or “at most two distinct”.

### Tips
- Use hashmap to store the last index of each character in the window.
- When size exceeds `k`, remove the character with the smallest last index.

### Template
```python
left = 0
seen = {}
best = 0

for right, ch in enumerate(s):
    seen[ch] = right
    if len(seen) > k:
        drop_char = min(seen, key=seen.get)
        left = seen[drop_char] + 1
        del seen[drop_char]
    best = max(best, right - left + 1)
```

### Problems
- 0159 Longest Substring with At Most Two Distinct Characters
- 0340 Longest Substring with At Most K Distinct Characters

---

## Pattern 4: Frequency Map / Counter in Sliding Window

### When to Use
- Need to track counts of elements in the window.

### How to Recognize
- Problem requires knowing the frequency of elements inside the window.

### Tips
- Use `collections.Counter` or dict to manage counts.
- Remove elements when count drops to zero.

### Template
```python
from collections import Counter

left = 0
counter = Counter()

for right, ch in enumerate(s):
    counter[ch] += 1
    while condition_not_satisfied:
        counter[s[left]] -= 1
        if counter[s[left]] == 0:
            del counter[s[left]]
        left += 1
```

### Problems
- 0904 Fruit Into Baskets
- 2444 Count Subarrays With Fixed Bounds

---

## Pattern 5: Sliding Window with Sorting or Binary Search

### When to Use
- Condition depends on sorted order inside the window.

### How to Recognize
- Requires median, order statistics, or binary search on window elements.

### Tips
- Use balanced BST or bisect in Python for insertion/removal.
- This is usually `O(n log n)`.

### Problems
- 1838 Frequency of the Most Frequent Element

---

## Keywords & How to Recognize Sliding Window
- Keywords: “subarray”, “substring”, “consecutive”, “contiguous”.
- Often involves finding max/min/average/count over a continuous segment.
- Usually requires two pointers `left` and `right` moving forward only.
