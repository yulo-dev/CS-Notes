# method 1: Min Heap
# space complexity: O(k)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min heap to keep track of the smallest current node from each list
        heap = []

        # Step 1: Initialize the heap with the head node of each list
        for i, node in enumerate(lists):
            if node:
                # Each heap item: (node value, list index, node object)
                # The list index is used to break ties when values are equal
                heapq.heappush(heap, (node.val, i, node))

        # Step 2: Create a dummy node to simplify result list construction
        dummy = ListNode(0)
        current = dummy  # Pointer to build the merged list

        # Step 3: Continuously extract the smallest node and add to the result
        while heap:
            val, i, node = heapq.heappop(heap)  # Get the node with the smallest value

            current.next = node  # Attach this node to the result list
            current = current.next  # Move the pointer forward

            if node.next:
                # If the current node has a next node, push it into the heap
                heapq.heappush(heap, (node.next.val, i, node.next))

        # Step 4: Return the head of the merged list (skip dummy node)
        return dummy.next


# method 2: Pairwise Merge
# space complexity: O(log k)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        # Step 1: Divide - split the list into two halves
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        # Step 2: Conquer - merge two sorted lists
        return self.mergeTwoLists(left, right)

    # Standard merge function (from Leetcode 21)
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Attach the remaining nodes
        tail.next = l1 or l2
        return dummy.next
