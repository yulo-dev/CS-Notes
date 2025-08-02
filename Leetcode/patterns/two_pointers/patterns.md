
# Two Pointers Patterns 

---

## Pattern 1: Opposite Ends (Converging Pointers)
### When to Use
- Problems involving symmetry or mirrored comparisons.
- Common in palindrome checks or mirrored string/array problems.
- Often appears in string processing (e.g., palindrome, mirrored digit) or numeric array symmetry.

### Template
```python
left, right = 0, len(arr)-1
while left < right:
    if condition(arr[left], arr[right]):
        left += 1
        right -= 1
    else:
        # handle mismatch
        ...
```

### Example Problems
- **LC 680 Valid Palindrome II** → check palindrome allowing one mismatch removal.
- **LC 246 Strobogrammatic Number** → verify mirrored digits mapping (e.g., 6↔9, 8↔8).
- **LC 1842 Next Palindrome Using Same Digits** → generate next greater palindrome using half permutation and mirroring.
- **LC 2193 Minimum Number of Moves to Make Palindrome** → greedy swaps to match mirrored positions.

### Tips
- Keywords: "palindrome", "symmetric", "mirror", "remove at most one".
- For mismatch handling, consider skipping left or right pointer.
- For digit/character mapping, prepare a dictionary (e.g., {'6':'9', '9':'6'}).

---

## Pattern 2: Fast & Slow Pointers (Runner Technique)
### When to Use
- Linked list problems involving relative positions.
- Finding nth node from end, detecting cycle, or finding middle.

### Template
```python
fast = slow = head
for _ in range(n):  # move fast ahead
    fast = fast.next

while fast:
    fast = fast.next
    slow = slow.next
# slow is now at desired node
```

### Example Problems 
- **LC 19 Remove Nth Node from End of List** → maintain n-gap between fast and slow pointers to locate target.

### Tips
- Keywords: "nth from end", "middle of list", "detect cycle".
- If detecting cycles → use while fast and fast.next, move fast by 2, slow by 1.

---

## Pattern 3: Merge Type (Two Arrays Sync)
### When to Use
- Working with two sorted lists or arrays.
- Finding intersections, merging results, or choosing optimal path sums.

### Template
```python
i = j = 0
while i < len(A) and j < len(B):
    if A[i] < B[j]:
        process(A[i])
        i += 1
    elif A[i] > B[j]:
        process(B[j])
        j += 1
    else:
        sync_process(A[i], B[j])
        i += 1
        j += 1
# process remaining
```

### Example Problems 
- **LC 1537 Get the Maximum Score** → sync traversal at intersections, accumulate path sums, choose max.

### Tips
- Keywords: "merge", "intersection", "two sorted arrays".
- Always handle remaining elements after one array is exhausted.

---

## Pattern 4: Pointer Offset (Meeting Point)
### When to Use
- Equalize traversal length between two linked structures.
- Detect intersection or meeting node without extra space.

### Template
```python
a, b = p, q
while a != b:
    a = a.next if a else q
    b = b.next if b else p
return a  # intersection node or None
```

### Example Problems 
- **LC 1650 Lowest Common Ancestor of a Binary Tree III** → treat parent pointers like linked list heads, find intersection.

### Tips
- Keywords: "two nodes", "find intersection", "parent pointer".
- Works because path lengths are equalized by switching heads.

---

## Pattern 5: Greedy Matching (String Swaps)
### When to Use
- Reorder characters to achieve palindrome or matching structure with minimal moves.
- Often combined with two pointers for pairing.

### Template (Palindrome swap example)
```python
s = list(s)
left, right = 0, len(s)-1
while left < right:
    i = right
    while i > left and s[i] != s[left]:
        i -= 1
    if i == left:  # no match, swap adjacent
        s[left], s[left+1] = s[left+1], s[left]
        res += 1
    else:
        for j in range(i, right):
            s[j], s[j+1] = s[j+1], s[j]
            res += 1
        left += 1
        right -= 1
```

### Example Problems
- **LC 2193 Minimum Number of Moves to Make Palindrome** → greedily swap unmatched char towards center.

### Tips
- Keywords: "minimum moves", "palindrome", "string reordering".
- For one unmatched char → move towards center.

---

## Pattern 6: Sorting + Two Pointers (Pair Sums)
### When to Use
- Pair elements meeting specific criteria (e.g., sum < target).
- Requires sorted input for efficient traversal.

### Template
```python
arr.sort()
left, right = 0, len(arr)-1
while left < right:
    if arr[left] + arr[right] < target:
        count += right - left
        left += 1
    else:
        right -= 1
```

### Example Problems 
- **LC 2824 Count Pairs Whose Sum is Less than Target** → sort and count valid pairs.

### Tips
- Keywords: "count pairs", "sum < target", "sorted array".
- Move left pointer when condition is satisfied to count in bulk.

---

## Pattern 7: String Processing (Index Jump / Two Pointers)
### When to Use
- String tasks that need skipping or jumping over indices.
- Often applied when parsing patterns or reversing words.

### Template
```python
i = j = 0
while i < len(pattern) and j < len(word):
    # jump based on rules or compare
    ...
```

### Example Problems
- **LC 151 Reverse Words in a String** → trim spaces, reverse word order using two-pointer scanning.
- **LC 408 Valid Word Abbreviation** → parse abbreviation vs actual word by skipping digits.
- **LC 3406 Find the Lexicographically Largest String From Box II** → scan and conditionally reorder substring.

### Tips
- Keywords: "parse", "reverse words", "abbreviation", "lexicographic".
- Often combined with split/join but can be solved in-place with pointers.

---

## Pattern 8: Dutch National Flag (Partitioning)
### When to Use
- Reordering elements by category in place.
- Typically used for problems asking to sort three groups.

### Template
```python
low, mid, high = 0, 0, len(nums)-1
while mid <= high:
    if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1; mid += 1
    elif nums[mid] == 1:
        mid += 1
    else:
        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1
```

### Example Problems 
- **LC 75 Sort Colors** → reorder three colors using three pointers.

### Tips
- Keywords: "three categories", "sort in place", "constant space".
- Careful with while conditions to avoid infinite loops.

---

## Notes
- Two Pointers is a technique family: Opposite Ends, Fast & Slow, Merge Sync, Pointer Offset, Greedy Matching, Sorting + Pair Sums, String Processing, Partitioning.
- Many Sliding Window problems (like Longest Substring Without Repeating Characters) extend from Two Pointers but include additional state (set/map).
- Recognize keywords in problem statements to quickly map to patterns.
