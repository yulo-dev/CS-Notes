
# check cycle + get the entry: 142 & 287

slow = fast = head

  # step 1: check cycle
  while fast and fast.next:
     slow = slow.next
     fast = fest.next.next
            
  # if there's a cycle
     if slow == fast:
  # step 2: check entry
        slow = head
        while slow != fast:
           slow = slow.next
           fast = fest.next
           return slow
      
  return None


# check cycle + reverse linkedlist + check palindrome or check max sum: 234, 2130

slow = fast = head

# step 1: check cycle
curr = head
while curr:
  slow = slow.next
  fast = fast.next.next

# step 2: reverse linkedlist
prev = None
while slow:
  nxt = slow.next
  slow.next = prev
  prev = slow
  slow = nxt

# step 3: do the checking
left = head
right = prev
while right:
  do some checking rules
  left = left.next
  right = right.next

return xxx
