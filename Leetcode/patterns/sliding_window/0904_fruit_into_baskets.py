# solution 1: Naive Brute Force (TLE in big input)
# Time Complexity: Worst case O(n²) — nested loop for each subarray

# Brute-force: Check all possible windows with at most 2 types
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_len = 0
        n = len(fruits)

        for i in range(n):
            fruit_types = set()
            for j in range(i, n):
                fruit_types.add(fruits[j])

                # If we have more than 2 types, break
                if len(fruit_types) > 2:
                    break

                # Otherwise update max length
                max_len = max(max_len, j - i + 1)

        return max_len




# solution 2: Intermediate Sliding Window with Counter
# Time Complexity: O(n)

# Use sliding window and Counter to track fruit types and counts
from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_len = 0
        count = Counter()

        for right in range(len(fruits)):
            count[fruits[right]] += 1  # Add fruit to the basket

            # Shrink window if we have more than 2 types
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]  # Remove type from basket
                left += 1

            # Update max window size
            max_len = max(max_len, right - left + 1)

        return max_len




# solution 3: Optimized Sliding Window with HashMap
# Time Complexity: O(n)

# Optimized version: Only track last seen index for each fruit
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        visited = {}   # {fruit_type: last_seen_index}
        left = 0
        max_len = 0

        for right in range(len(fruits)):
            fruit = fruits[right]
            visited[fruit] = right  # Update last seen index

            # If we have more than 2 types, shrink the window
            if len(visited) > 2:
                # Find the fruit with the earliest last seen index
                oldest = min(visited, key=visited.get)
                left = visited[oldest] + 1
                del visited[oldest]

            max_len = max(max_len, right - left + 1)

        return max_len
