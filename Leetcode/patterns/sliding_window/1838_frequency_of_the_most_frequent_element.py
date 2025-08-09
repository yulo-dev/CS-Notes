# solution1: brute force
# time complexity: O(n³)
# space complexity: O(1)

class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        # Brute force:
        # 1) Sort so the right end is the window max.
        # 2) Enumerate every window [l..r].
        # 3) Compute sum(nums[l:r+1]) from scratch (O(n)).
        # 4) Cost to raise all to nums[r] is val*len - window_sum.
        # 5) If cost <= k, update answer.

        nums.sort()
        n = len(nums)
        best = 1

        for r in range(n):
            val = nums[r]              # target = window max after sorting
            for l in range(r + 1):
                length = r - l + 1
                window_sum = sum(nums[l:r+1])  # O(n) each time
                cost = val * length - window_sum
                if cost <= k:
                    best = max(best, length)

        return best

# solution 2: sliding window
# time complexity: O(n log n)
# space complexity: O(1)

class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        # Core idea:
        # After sorting, for each right end r (target = nums[r]),
        # the cheapest way is to raise all numbers in the window [l..r] up to nums[r].
        # Cost to make all equal to val = val * window_len - window_sum.
        # If cost > k, shrink from the left.

        nums.sort()  # Ensure nums[r] is the max in the window
        l = 0
        window_sum = 0  # Sum of current window [l..r]
        best = 1

        for r, val in enumerate(nums):
            # Expand window by including nums[r]
            window_sum += val

            # While the cost to raise all elements to val exceeds k, shrink from left
            # cost = val * window_len - window_sum
            while val * (r - l + 1) - window_sum > k:
                window_sum -= nums[l]
                l += 1

            # Update the best (max frequency)
            best = max(best, r - l + 1)

        return best

      
# solution 3: Sort + Prefix Sum + Binary Search
# time complexity: O(n log n)
# space complexity: O(n)

class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        # Idea:
        # Precompute prefix sums to query window_sum in O(1).
        # For each r, binary search the smallest l such that
        # cost = nums[r] * (r - l + 1) - window_sum(l..r) <= k.
        # This demonstrates the same formula with a different technique.

        nums.sort()
        n = len(nums)

        # prefix[i] = sum of nums[0..i-1]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def window_sum(l: int, r: int) -> int:
            # Sum of nums[l..r]
            return prefix[r + 1] - prefix[l]

        best = 1

        for r in range(n):
            val = nums[r]

            # Binary search l in [0..r]
            lo, hi = 0, r
            ans_l = r  # fallback: at least the single element window

            while lo <= hi:
                mid = (lo + hi) // 2
                length = r - mid + 1
                cost = val * length - window_sum(mid, r)

                if cost <= k:
                    # mid is feasible, try to extend more (move left further)
                    ans_l = mid
                    hi = mid - 1
                else:
                    # too expensive, need to move right (shrink)
                    lo = mid + 1

            best = max(best, r - ans_l + 1)

        return best
