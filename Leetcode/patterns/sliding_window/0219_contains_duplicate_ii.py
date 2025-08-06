# solution 1: brute force
# Time Complexity: O(n * k) in worst case
# Space Complexity: O(1)
# Notes: Will time out for large inputs. 

# Brute Force: Check all pairs within distance k
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, min(i + k + 1, n)):
                # Check if the values are the same and indices within range k
                if nums[i] == nums[j]:
                    return True
        return False


# solution 2: sliding window + hashset
# Time Complexity: O(n)
# Space Complexity: O(k)
# Checks only within the last k elements efficiently

# Optimized: Sliding window of size k using a HashSet
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()  # Tracks elements in the current sliding window
        left = 0

        for right in range(len(nums)):
            # If the current element already exists in the window, it's a duplicate
            if nums[right] in seen:
                return True

            # Add current element to the window
            seen.add(nums[right])

            # If window size exceeds k, remove the leftmost element
            if right - left >= k:
                seen.remove(nums[left])
                left += 1

        return False

