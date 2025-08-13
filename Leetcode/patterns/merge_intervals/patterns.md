# Merge Intervals — Patterns Summary

This guide consolidates common **interval** patterns you’ll see across LeetCode. It teaches you **when to use which pattern**, **how to recognize** the right approach, core **tips/pitfalls**, a short **template**, and **example problems** you’ve solved.

---

## Pattern 1 — Merge Overlapping Intervals (Sort + Single Pass)

### When to Use
- You’re given a list of intervals and asked to **merge overlaps** and return non-overlapping intervals.
- Typical ask: “merge”, “combine”, “return non-overlapping cover”.

### How to Recognize
- Input is a list of `[start, end]` intervals.
- The output should be a **new set of merged intervals** (not a count).
- Sorting by **start** immediately simplifies the process.
- Overlap condition depends on **current start** vs **last merged end**.

### Tips / Pitfalls
- Sort by `(start)` only; if ties occur, consider sorting by `(start, end)` for predictability.
- **Overlap test**: usually `start <= merged_last_end` merges; use `>` when you want to treat **touching** as merged or not based on the problem statement.
- If the problem uses half-open `[s, e)` semantics, equality handling can differ.
- Keep it **single pass** after sorting. No nested loops.

### Template
```python
intervals.sort(key=lambda x: x[0])
merged = []

for s, e in intervals:
    if not merged or s > merged[-1][1]:         # no overlap
        merged.append([s, e])
    else:                                       # overlap -> extend
        merged[-1][1] = max(merged[-1][1], e)
```

### Problems
- **0056 – Merge Intervals**
- **0057 – Insert Interval** (first insert, then the same merge pass)

---

## Pattern 2 — Insert + Merge (Insert Interval)

### When to Use
- You’re given a **sorted, non-overlapping** interval list and **one new interval**; return the merged result.

### How to Recognize
- “Insert an interval” into a **sorted** non-overlapping set.
- The key is to **place** then **merge touching/overlapping** parts.

### Tips / Pitfalls
- Append all intervals that end **before** the new interval starts.
- Merge all intervals that **overlap** the new interval while expanding `[start, end]`.
- Finally append the **rest**.
- Take care with off-by-one and equality (touching vs overlapping).

### Template
```python
res = []
i = 0
n = len(intervals)
ns, ne = newInterval

# Left of new
while i < n and intervals[i][1] < ns:
    res.append(intervals[i])
    i += 1

# Merge overlaps with new
while i < n and intervals[i][0] <= ne:
    ns = min(ns, intervals[i][0])
    ne = max(ne, intervals[i][1])
    i += 1
res.append([ns, ne])

# Right of new
while i < n:
    res.append(intervals[i])
    i += 1
```

### Problems
- **0057 – Insert Interval**

---

## Pattern 3 — Counting Concurrent Intervals (Minimum Resources)

### When to Use
- Ask: “**Minimum number of rooms/resources** to schedule all intervals?”
- Equivalent to **maximum number of overlaps at any time**.

### How to Recognize
- You’re not asked to output merged intervals—**you output a number** (capacity).
- Phrases: “minimum number of meeting rooms”, “cars never exceed capacity”, “max simultaneous events”.

### Two Main Approaches

#### A) Two Pointers on Sorted Starts & Ends (Sweep Line)
- Extract `starts` and `ends`, sort both.
- Walk with two pointers; compare `starts[i]` vs `ends[j]`.
- If `start < end`: need new resource; else: free one.
```python
starts = sorted(s for s, _ in intervals)
ends   = sorted(e for _, e in intervals)
i = j = 0
rooms = ans = 0
while i < len(starts):
    if starts[i] < ends[j]:
        rooms += 1
        ans = max(ans, rooms)
        i += 1
    else:
        rooms -= 1
        j += 1
# ans is the minimum number of rooms
```

#### B) Min-Heap by End Time
- Sort by start; heap keeps **current end times**.
- Pop all ended intervals (`end <= start`) before pushing the new one.
```python
import heapq
intervals.sort(key=lambda x: x[0])
heap = []
ans = 0
for s, e in intervals:
    while heap and heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap, e)
    ans = max(ans, len(heap))
```

### Tips / Pitfalls
- Equality handling (`start == end`): for half-open `[s, e)` you can **free first** (treat as no extra room).
- For discrete small coordinate ranges, **difference array / prefix sum** can be simpler.

### Problems
- **0253 – Meeting Rooms II** (rooms count)
- **1094 – Car Pooling** (also solvable with **difference array** over small range)

---

## Pattern 4 — Difference Array / Prefix Sum on Timeline

### When to Use
- When time/location domain is **small and integer** (e.g., stops 0–1000).
- You need to **accumulate** adds/removes and check a threshold/capacity.

### How to Recognize
- Problem gives a **bounded index range** and frequent “add at start, remove at end” semantics.
- Ask is often: “does capacity ever exceed X?”

### Tips / Pitfalls
- For each interval `[s, e)`: `diff[s] += val`, `diff[e] -= val`.
- Running prefix `curr += diff[i]`; check/record max on the fly.
- Ensure you understand whether the end is **exclusive** or **inclusive**.

### Template (capacity check)
```python
MAX = 1000  # example domain bound
diff = [0]*(MAX+1)
for val, s, e in trips:   # or (s, e) for +1/-1
    diff[s] += val
    diff[e] -= val
curr = 0
for x in range(MAX+1):
    curr += diff[x]
    if curr > capacity:
        return False
return True
```

### Problems
- **1094 – Car Pooling**

---

## Pattern 5 — Interval Intersections (Two Sorted Lists)

### When to Use
- Given **two sorted** interval lists, find all **intersections**.
- Output the **intersection intervals**, not a count.

### How to Recognize
- Two pointer walking of two sorted lists.
- At each step, the intersection is `[max(starts), min(ends)]` if `lo <= hi`.

### Tips / Pitfalls
- Always advance the pointer with the **smaller end** (it cannot intersect further).
- Handle touching intervals according to problem spec (`<=` vs `<`).

### Template
```python
i = j = 0
res = []
while i < len(A) and j < len(B):
    lo = max(A[i][0], B[j][0])
    hi = min(A[i][1], B[j][1])
    if lo <= hi:
        res.append([lo, hi])
    if A[i][1] < B[j][1]:
        i += 1
    else:
        j += 1
```

### Problems
- **0986 – Interval List Intersections**

---

## Pattern 6 — Remove Covered (Filtering by Envelope)

### When to Use
- Count or return intervals that are **not entirely covered** by another interval.

### How to Recognize
- Wording includes: “remove covered intervals”, “count remaining after removing enclosed ones”.

### Tips / Pitfalls
- Sort by `(start ASC, end DESC)` so longer intervals come first for same `start`.
- Keep a running `max_end` and count intervals with `end > max_end`.
- If `end <= max_end` → covered; otherwise keep and update `max_end`.

### Template
```python
intervals.sort(key=lambda x: (x[0], -x[1]))
count = 0
max_end = -10**18
for s, e in intervals:
    if e > max_end:   # not covered
        count += 1
        max_end = e
# 'count' is intervals remaining (not covered)
```

### Problems
- **1288 – Remove Covered Intervals**

---

## Pattern 7 — Counting Days Without Meetings (Gap Accumulation)

### When to Use
- Union the busy intervals, then **sum gaps** or **sum free lengths** in a range.

### How to Recognize
- You’re asked to count **free time** (e.g., days without meetings).
- Equivalent to: merge the intervals, then compute the complement measure.

### Tips / Pitfalls
- First **merge** busy intervals (Pattern 1).
- Then accumulate gaps between consecutive merged intervals (respect bounds if provided).

### Template
```python
# 1) Merge busy intervals
intervals.sort(key=lambda x: x[0])
merged = []
for s, e in intervals:
    if not merged or s > merged[-1][1]:
        merged.append([s, e])
    else:
        merged[-1][1] = max(merged[-1][1], e)

# 2) Sum gaps (optionally within [L, R])
free = 0
for i in range(1, len(merged)):
    free += max(0, merged[i][0] - merged[i-1][1])
```

### Problems
- **3169 – Count Days Without Meetings**

---

## Quick Recognition 

- **“Merge/Combine intervals”** → Pattern 1 (Sort + Single Pass).  
- **“Insert an interval into sorted non-overlapping set”** → Pattern 2.  
- **“Minimum rooms/resources / Max concurrent”** → Pattern 3 (Two Pointers or Min-Heap).  
- **“Bounded index timeline with adds/removes; capacity check”** → Pattern 4 (Difference Array).  
- **“Intersection of two sorted interval lists”** → Pattern 5 (Two Pointers).  
- **“Remove covered/enclosed intervals”** → Pattern 6 (Sort by start asc, end desc).  
- **“Count free/gap days after union”** → Pattern 7 (Merge then accumulate gaps).  

---

## General Ideas

- Decide early: **Are ends inclusive or exclusive?** (`[s,e]` vs `[s,e)`). This changes equality checks.
- Sorting is almost always step 1. Choose the **secondary key** carefully to simplify scans.
- Prefer **linear passes** after sorting; avoid nested loops.
- For counts of concurrent intervals, think in **events** (starts = +1, ends = −1) and **sweep**.
- When memory/time allows, min-heap is a clean alternative to two-pointer sweeping.
- For bounded discrete domains, **difference arrays** are simple and fast.

---

## Problems Mapped

- **0056 – Merge Intervals** → Pattern 1  
- **0057 – Insert Interval** → Pattern 2 (+ Pattern 1 merge at the end)  
- **0253 – Meeting Rooms II** → Pattern 3 (Two Pointers / Min-Heap)  
- **0986 – Interval List Intersections** → Pattern 5  
- **1094 – Car Pooling** → Pattern 4 (Difference Array) or Pattern 3 (Heap)  
- **1288 – Remove Covered Intervals** → Pattern 6  
- **3169 – Count Days Without Meetings** → Pattern 7 (Merge + gap sum)

---
