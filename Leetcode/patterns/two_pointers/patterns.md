
# Two Pointers Patterns 

---

## Pattern 1: Opposite Ends (Converging Pointers)
### Typical Input
String or array where elements from both ends need to be compared.
### Goal
Check for symmetry, palindromes, mirrored properties, or process pairs from opposite ends.
### When to Use
When a problem involves comparing elements from both ends and converging to the center.
### Key Idea (Trigger Words)
"palindrome", "symmetric", "mirror", "remove at most one"
### Template
```python
left, right = 0, len(arr) - 1
while left < right:
    if arr[left] == arr[right]:
        left += 1
        right -= 1
    else:
        # handle mismatch if allowed (skip one or return false)
        ...
```
### Example Problems
- LC 680 Valid Palindrome II → check palindrome allowing one mismatch removal.
- LC 246 Strobogrammatic Number → verify mirrored digits mapping (e.g., 6↔9, 8↔8).
- LC 1842 Next Palindrome Using Same Digits → generate next greater palindrome using half permutation and mirroring.
- LC 2193 Minimum Number of Moves to Make Palindrome → greedy swaps to match mirrored positions.
### Tips
- Build mapping for mirrored characters if needed (e.g., {'6':'9','9':'6'}).
- For mismatch handling, consider skipping either left or right pointer.

---

## Pattern 2: Fast & Slow Pointers (Runner Technique)
### Typical Input
Linked list or sequential data structure.
### Goal
Find nth node from the end, detect cycles, or find the middle of the list.
### When to Use
When relative positions or cycle detection in linked structures are required.
### Key Idea (Trigger Words)
"nth from end", "find middle", "detect cycle"
### Template
```python
fast = slow = head
for _ in range(n):  # move fast ahead by n
    fast = fast.next

while fast:
    fast = fast.next
    slow = slow.next
# slow is now at the target node
```
### Example Problems
- LC 19 Remove Nth Node from End of List → maintain n-gap between fast and slow pointers.
### Tips
- For cycle detection: move fast by 2 steps, slow by 1 step.
- For middle node: no initial gap, just move fast twice as fast.

---

## Pattern 3: Merge Type (Two Arrays Sync)
### Typical Input
Two sorted arrays (or sorted linked lists).
### Goal
Find intersections, merge sorted results, or compute combined values efficiently.
### When to Use
When two sorted structures need to be processed simultaneously.
### Key Idea (Trigger Words)
"two sorted arrays", "intersection", "merge"
### Template
```python
i = j = 0
while i < len(A) and j < len(B):
    if A[i] < B[j]:
        # process A[i]
        i += 1
    elif A[i] > B[j]:
        # process B[j]
        j += 1
    else:
        # handle intersection
        i += 1
        j += 1

# process remaining elements if required
```
### Example Problems
- LC 1537 Get the Maximum Score → sync traversal at intersections, accumulate path sums, choose max.
### Tips
- Ensure sorted inputs before applying this technique.
- Always handle remaining elements after one array finishes.

---

## Pattern 4: Pointer Offset (Meeting Point)
### Typical Input
Two linked lists or nodes with parent pointers forming chains.
### Goal
Find intersection node or meeting point regardless of different path lengths.
### When to Use
When two linked paths may differ in length and need equalized traversal.
### Key Idea (Trigger Words)
"find intersection", "two linked lists", "meeting node"
### Template
```python
a, b = p, q
while a != b:
    a = a.next if a else q
    b = b.next if b else p
return a  # intersection node or None
```
### Example Problems
- LC 1650 Lowest Common Ancestor of a Binary Tree III → treat parent pointers as linked list heads, find intersection.
### Tips
- Works because both pointers traverse equal total distance.
- Commonly used for linked list intersection (LC 160).

---

## Pattern 5: Greedy Matching (String Swaps)
### Typical Input
String needing reordering to meet palindrome or matching criteria.
### Goal
Reorder with minimal moves (e.g., to form palindrome).
### When to Use
When characters need to be paired or repositioned efficiently.
### Key Idea (Trigger Words)
"minimum moves", "palindrome", "string reordering"
### Template
```python
s = list(s)
left, right = 0, len(s) - 1
res = 0
while left < right:
    i = right
    while i > left and s[i] != s[left]:
        i -= 1
    if i == left:
        # no match, swap adjacent
        s[left], s[left+1] = s[left+1], s[left]
        res += 1
    else:
        # bubble matching char to right
        for j in range(i, right):
            s[j], s[j+1] = s[j+1], s[j]
            res += 1
        left += 1
        right -= 1
```
### Example Problems
- LC 2193 Minimum Number of Moves to Make Palindrome → greedily swap unmatched char toward center.
### Tips
- Only one unmatched char allowed for odd length palindrome.
- This method is O(n^2) worst-case but acceptable for interview.

---

## Pattern 6: Sorting + Two Pointers (Pair Sums)
### Typical Input
Array of numbers; target sum condition.
### Goal
Count or find pairs that meet specific sum criteria.
### When to Use
When sum comparison between pairs is required, often with sorted input.
### Key Idea (Trigger Words)
"count pairs", "sum < target", "sorted array"
### Template
```python
arr.sort()
count = 0
left, right = 0, len(arr) - 1
while left < right:
    if arr[left] + arr[right] < target:
        count += right - left
        left += 1
    else:
        right -= 1
```
### Example Problems
- LC 2824 Count Pairs Whose Sum is Less than Target → count valid pairs using sorted array.
### Tips
- Sorting ensures linear scanning.
- Useful for problems like 3Sum, 4Sum (with modifications).

---

## Pattern 7: String Processing (Index Jump / Two Pointers)
### Typical Input
String with pattern matching, abbreviation, or word reversal.
### Goal
Parse or reorder string using pointer jumps.
### When to Use
When string scanning and skipping are required (e.g., abbreviation parsing, reversing words).
### Key Idea (Trigger Words)
"parse", "reverse words", "abbreviation", "lexicographic"
### Template
```python
i = j = 0
while i < len(pattern) and j < len(word):
    # skip or process based on rules
    ...
```
### Example Problems
- LC 151 Reverse Words in a String → trim spaces, reverse word order.
- LC 408 Valid Word Abbreviation → parse abbreviation and match original word.
- LC 3406 Find the Lexicographically Largest String From Box II → scan and reorder substring conditionally.
### Tips
- Many string problems can use built-in split/join but two pointers enable in-place control.
- Carefully handle whitespace or digits when skipping.

---

## Pattern 8: Dutch National Flag (Partitioning)
### Typical Input
Array with three categories (e.g., 0/1/2 colors).
### Goal
Reorder elements by category in-place with O(1) space.
### When to Use
When elements belong to limited distinct groups that need grouping.
### Key Idea (Trigger Words)
"three categories", "partition", "in-place sort"
### Template
```python
low, mid, high = 0, 0, len(nums) - 1
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
- LC 75 Sort Colors → reorder three colors using three pointers.
### Tips
- Be careful with mid pointer updates when swapping with high.
- This is a classic partitioning problem; memorize its steps.

---

## Notes
- Two Pointers is a technique family: Opposite Ends, Fast & Slow, Merge Sync, Pointer Offset, Greedy Matching, Sorting + Pair Sums, String Processing, Partitioning.
- The two pointers pattern focuses on comparing data values, whereas the fast and slow pointers method is typically used to analyze the structure or properties of the data.
- Many Sliding Window problems (like Longest Substring Without Repeating Characters) extend from Two Pointers but include additional state (set/map).
- Recognize input type, goal, and keywords to quickly map to patterns during interviews.
