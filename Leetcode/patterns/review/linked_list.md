# Linked List Templates

## Core Data Structure

```python
from typing import List, Optional

class ListNode:
    def __init__(self, val: int = 0, next: 'Optional[ListNode]' = None):
        self.val = val
        self.next = next
```

## Helper Functions

### Array to Linked List
```python
def array_to_list(nums: List[int]) -> Optional[ListNode]:
    #用 dummy/tail 把陣列接成單向鏈表。空陣列回傳 None。
    dummy = ListNode(0)
    tail = dummy
    for x in nums:
        tail.next = ListNode(x)  # 接上新節點
        tail = tail.next         # 移動尾巴
    return dummy.next
```

### Linked List to Array
```python
def list_to_array(head: Optional[ListNode]) -> List[int]:
    #把鏈表轉回陣列，方便檢查
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    return ans
```

### Usage Example
```python
# 範例
head = array_to_list([10, 20, 30])
print(list_to_array(head))  # [10, 20, 30]
```

## Reverse Linked List Template

```python
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, cur = None, head
    while cur:
        nxt = cur.next # 1. 暫存下一個
        cur.next = prev # 2. 反轉指向
        prev, cur = cur, nxt # 3. 指標前進
    return prev # prev 是新頭
```

## Key Patterns to Remember

### 3 Steps for Reverse:
1. **保存next** - `nxt = cur.next`
2. **反轉指針** - `cur.next = prev`
3. **移動指針** - `prev, cur = cur, nxt`

## Review Problems
- **LeetCode 206**: Reverse Linked List (exact template match)
