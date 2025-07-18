# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node that points to the head
        # This simplifies edge cases like removing the first node
        dummy = ListNode(0, head)
        
        # Initialize two pointers: fast and slow
        fast = dummy
        slow = dummy

        # Move the fast pointer n steps ahead to create a gap
        for _ in range(n):
            fast = fast.next

        # Move both pointers together until fast reaches the end
        # At this point, slow is right before the node to delete
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove the target node by skipping it
        slow.next = slow.next.next

        # Return the new head (which might have changed)
        return dummy.next
