# solution 1: brute force
# For each starting index i, calculate the sum of the next k elements.
# Compare it to lower and upper to update the score.
# Inefficient for large input, since sum() in each iteration is O(k).
# time complexity: O(n * k)
# space complexity: O(1)

class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        score = 0
        n = len(calories)

        # Check every contiguous subarray of length k
        for i in range(n - k + 1):
            window_sum = sum(calories[i:i + k])  # O(k) operation

            if window_sum < lower:
                score -= 1
            elif window_sum > upper:
                score += 1

        return score

      
# solution 2: Optimized Sliding Window Version
# time complexity: O(n)
# space complexity: O(1)

class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        # Step 1: Compute the sum of the first window
        window_sum = sum(calories[:k])
        score = 0

        # Step 2: Evaluate the first window
        if window_sum < lower:
            score -= 1
        elif window_sum > upper:
            score += 1

        # Step 3: Slide the window across the array
        for i in range(k, len(calories)):
            # Subtract the leftmost value and add the new value on the right
            window_sum += calories[i] - calories[i - k]

            # Evaluate the new window
            if window_sum < lower:
                score -= 1
            elif window_sum > upper:
                score += 1

        return score
