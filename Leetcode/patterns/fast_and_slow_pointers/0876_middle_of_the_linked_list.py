# solution 1: two traversal

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Count length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Step 2: Find the middle index (second middle if even length)
        middle_index = length // 2
        
        # Step 3: Traverse again to the middle node
        current = head
        for _ in range(middle_index):
            current = current.next
        
        return current

# solution 2: Slow and Fast Pointers

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize slow and fast pointers
        slow = fast = head
        
        # Move fast by two steps and slow by one step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # When fast reaches the end, slow is at the middle
        return slow
