# solution 1: array + two pointers
# time: O(n)
# space: O(n) 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1: Convert linked list to array
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        # Step 2: Use two pointers from both ends to find max twin sum
        left, right = 0, len(values) - 1
        max_sum = 0
        while left < right:
            max_sum = max(max_sum, values[left] + values[right])
            left += 1
            right -= 1
        
        return max_sum

# solution 2: fast and slow pointers (find mid + reverse second half)
# time: O(n)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1: Use fast and slow pointers to find the middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        # Step 3: Compare values from the start and from reversed half
        max_sum = 0
        left, right = head, prev
        while right:  # Only need to traverse half length
            max_sum = max(max_sum, left.val + right.val)
            left = left.next
            right = right.next
        
        return max_sum
