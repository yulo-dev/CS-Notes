class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 10**9 + 7  # required modulo for the final result
        i = j = 0        # two pointers for nums1 and nums2
        sum1 = sum2 = 0  # cumulative sums for each path (nums1 path, nums2 path)

        # Traverse both arrays until one of them ends
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                # nums1 element is smaller, move pointer i and add to sum1
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                # nums2 element is smaller, move pointer j and add to sum2
                sum2 += nums2[j]
                j += 1
            else:
                # Intersection point (same value in both arrays)
                # Choose the better path so far and add the intersection value
                best = max(sum1, sum2) + nums1[i]
                sum1 = sum2 = best  # synchronize both sums at intersection
                i += 1
                j += 1

        # Add remaining elements in nums1 (if nums2 finished first)
        while i < len(nums1):
            sum1 += nums1[i]
            i += 1

        # Add remaining elements in nums2 (if nums1 finished first)
        while j < len(nums2):
            sum2 += nums2[j]
            j += 1

        # Return the larger sum path and take modulo
        return max(sum1, sum2) % mod
