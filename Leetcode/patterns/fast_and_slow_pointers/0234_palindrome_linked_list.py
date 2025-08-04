# solution 1: Array
# Time: O(n) (traverse + comparison)
# Space: O(n) (array storage)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Approach 1: Convert linked list to an array
        values = []
        
        # Traverse linked list and store values in array
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        # Use two pointers to check palindrome
        left, right = 0, len(values) - 1
        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1
        
        return True



# solution 2: Fast and Slow Pointers (Reverse Second Half)
# Time: O(n) (find middle + reverse + compare)
# Space: O(1) (no extra structure, only a few pointers)

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # Step 1: Find the middle using fast & slow pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            nxt = slow.next    # Store next node
            slow.next = prev   # Reverse pointer
            prev = slow        # Move prev forward
            slow = nxt         # Move slow forward
        
        # Step 3: Compare first half and reversed second half
        left, right = head, prev
        while right:  # Only need to check second half length
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
