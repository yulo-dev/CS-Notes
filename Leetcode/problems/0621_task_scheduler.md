# Leetcode 0621 - Task Scheduler

## ☀️ UMPIRE
- **Understand**: Given a list of tasks and an integer `n`, return the least number of time units that the CPU will take to finish all the tasks. Same tasks must be at least `n` units apart. Each task takes exactly 1 time unit. Idle time is allowed.
- **Match**: Frequency-counting problem with cooldown constraints. Greedy pattern, or can simulate with heap.
- **Plan**: Count frequencies, find max frequency and how many tasks share it. Use formula to compute minimum time or simulate with heap.
- **Implement**: See both optimized (math) and heap-based implementations below.
- **Review**: Watch for off-by-one errors in formula. Ensure cooldown logic is respected.
- **Evaluate**:  
  - Time Complexity: O(n + k) in both versions (n = number of tasks, k = number of unique tasks ≤ 26).  
  - Space Complexity:
    - `list().count()` version: O(k) due to copying task_counts.values() into a list.
    - single-pass version: O(1), no extra space used beyond basic counters.

## ☀️ Metadata
- **Appears In**: Grind75
- **Pattern**: Greedy / Scheduling
- **Data Structure**: Hash Map (Counter), Priority Queue (optional)
- **Algorithm**: Greedy Math or Heap Simulation
- **Tags**: Greedy, Heap, Simulation, Counting


## ☀️ Solution Code: Optimized Math Method

```python
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count task frequencies
        task_counts = Counter(tasks)

        # Find the maximum frequency
        max_freq = max(task_counts.values())

        # Count how many tasks have that maximum frequency
        max_count = list(task_counts.values()).count(max_freq)

        # Compute the minimal intervals needed using the greedy formula
        intervals = (max_freq - 1) * (n + 1) + max_count

        # Return the larger of the intervals or the number of tasks
        return max(len(tasks), intervals)
```

## ☀️ Solution Code: Optimized Math Method (Single Pass)

```python
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_freq = 0
        max_count = 0

        # Single pass to find both max_freq and its count
        for freq in task_counts.values():
            if freq > max_freq:
                max_freq = freq
                max_count = 1
            elif freq == max_freq:
                max_count += 1

        intervals = (max_freq - 1) * (n + 1) + max_count
        return max(len(tasks), intervals)
```


## ☀️ Complexity Comparison

| Aspect              | list().count() Version    | Single-Pass Version         |
|---------------------|----------------------------|------------------------------|
| Time Complexity     | O(n) + O(k)                | O(n) + O(k)                  |
| Space Complexity    | O(k) (list copy)           | O(1) (no extra structure)    |
| Readability         | High                       | Medium                       |
| Performance         | Slightly slower            | Slightly faster              |

> Here, `n` is total number of tasks, and `k` is the number of unique task types (at most 26).


## ☀️ Line-by-line Typing Script (Optimized Version)

- First, we count the frequency of each task using Counter.
- Then we compute the highest frequency of any task using max().
- We also count how many tasks have this max frequency.
- Based on the greedy formula, we compute how many slots we need to schedule these high-frequency tasks with cooldowns.
- Finally, we return the maximum between the computed interval count and the total number of tasks (in case no idle time is needed).
