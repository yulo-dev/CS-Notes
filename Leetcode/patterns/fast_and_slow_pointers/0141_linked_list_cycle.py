# solution 1: hashset
# Time: O(n) → We visit each node at most once
# Space: O(n) → Need a set to store visited nodes

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Use a set to keep track of visited nodes
        seen = set()
        current = head

        # Traverse the linked list
        while current:
            # If we have seen this node before, there is a cycle
            if current in seen:
                return True
            # Mark this node as visited
            seen.add(current)
            # Move to the next node
            current = current.next

        # If we reach None, there is no cycle
        return False


# solution 2: Fast & Slow Pointers (Floyd’s Cycle Detection)
# Time: O(n) → Each pointer visits nodes at most O(n) times
# Space: O(1) → Only two pointers used, no extra memory

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers at the head
        slow = fast = head

        # Iterate until fast pointer reaches the end (no cycle) 
        while fast and fast.next:
            # Move slow pointer by 1 step
            slow = slow.next
            # Move fast pointer by 2 steps
            fast = fast.next.next

            # If slow and fast meet, there is a cycle
            if slow == fast:
                return True

        # If fast reaches None, there is no cycle
        return False
