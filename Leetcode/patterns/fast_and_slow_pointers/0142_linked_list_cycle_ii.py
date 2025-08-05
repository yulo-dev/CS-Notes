# solution 1: HashSet
# Time Complexity: O(n)
# Space Complexity: O(n) (store visited nodes)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()  # store visited nodes
        
        current = head
        while current:
            # If we have already seen this node, cycle entry found
            if current in visited:
                return current
            visited.add(current)
            current = current.next
        
        return None  # no cycle


# solution 2: Fast and Slow Pointer (Floyd’s Tortoise and Hare)
# Time Complexity: O(n)
# Space Complexity: O(1) (only two pointers)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Detect if a cycle exists
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:  # cycle detected
                # Step 2: Find cycle entry
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow  # cycle entry node
        
        return None  # no cycle
