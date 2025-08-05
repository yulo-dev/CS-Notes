# solution 1: Naive Approach: Break the Circular List into a Linear List and Rebuild

def splitCircularLinkedList(head):
    # Edge case: empty list or single node
    if not head or head.next == head:
        return [head, None]

    # Step 1: Break the circle -> make it a normal linked list
    tail = head
    while tail.next != head:
        tail = tail.next
    tail.next = None  # break the circle

    # Step 2: Count total length
    length = 0
    node = head
    while node:
        length += 1
        node = node.next

    # Step 3: Find the midpoint index (ceil(n/2))
    mid = (length + 1) // 2

    # Step 4: Traverse to the midpoint
    node = head
    for _ in range(mid - 1):
        node = node.next

    # Step 5: Split the list into two halves
    second = node.next
    node.next = None  # end the first half

    # Step 6: Make both halves circular again
    # Close first half
    tail1 = head
    while tail1.next:
        tail1 = tail1.next
    tail1.next = head

    # Close second half
    tail2 = second
    while tail2 and tail2.next:
        tail2 = tail2.next
    if tail2:
        tail2.next = second

    return [head, second]


# solution 2: Two-Pass Approach: Find Midpoint, Split, Then Locate Second Tail

def splitCircularLinkedList(head):
    # Edge case: empty list or single node
    if not head or head.next == head:
        return [head, None]

    # Initialize slow and fast pointers
    slow = fast = head

    # Move fast by two steps and slow by one step to find midpoint
    while fast.next != head and fast.next.next != head:
        slow = slow.next
        fast = fast.next.next

    # First half head = original head
    head1 = head
    # Second half head = node after slow
    head2 = slow.next

    # Close the first half
    slow.next = head1

    # Traverse second half to find its tail
    temp = head2
    while temp.next != head:
        temp = temp.next

    # Close the second half
    temp.next = head2

    return [head1, head2]


＃solution 3: Optimized One-Pass Approach: Use Fast Pointer to Identify Tail Directly

def splitCircularLinkedList(head):
    # Edge case: empty list or single node
    if not head or head.next == head:
        return [head, None]

    # Initialize slow and fast pointers
    slow = fast = head

    # Move slow by one and fast by two steps until fast is about to loop back
    while fast.next != head and fast.next.next != head:
        slow = slow.next
        fast = fast.next.next

    # For odd-length lists, fast might stop one node before tail
    # Move it one step forward so it points to the actual last node
    if fast.next != head:
        fast = fast.next

    # Second half head is node after slow
    second = slow.next

    # Close the second half circle
    fast.next = second

    # Close the first half circle
    slow.next = head

    return [head, second]
