# version 1: list().count()
# space complexity: O(k), k represents the number of unique tasks — that is, the number of distinct characters in the input list.
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        task_counts = Counter(tasks)

        # Get the maximum frequency among all tasks
        max_freq = max(task_counts.values())

        # Count how many tasks have this maximum frequency
        # Convert dict_values to list to use .count()
        max_count = list(task_counts.values()).count(max_freq)

        # Calculate the minimum time required:
        # (max_freq - 1) blocks, each of size (n + 1), plus the number of max frequency tasks
        intervals = (max_freq - 1) * (n + 1) + max_count

        # The result is the maximum between intervals and the total number of tasks
        return max(len(tasks), intervals)


# version 2: single pass loop
# space complexity: O(1)
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        task_counts = Counter(tasks)

        # Initialize variables to track max frequency and number of tasks with that frequency
        max_freq = 0
        max_count = 0

        # One-pass loop to find both values without extra space
        for freq in task_counts.values():
            if freq > max_freq:
                max_freq = freq
                max_count = 1
            elif freq == max_freq:
                max_count += 1

        # Same formula as before
        intervals = (max_freq - 1) * (n + 1) + max_count

        return max(len(tasks), intervals)
