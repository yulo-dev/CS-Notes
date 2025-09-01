# BFS Level Order Traversal Template

## Core Template Structure

```python
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:
            level = []   # ← 每層要輸出的容器（換成鏈表etc.）
            
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val) # ← 這一行換成題目要的操作

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level # ← 每層結束時收集結果
        return res
```

## Key Components to Remember

1. **Import**: `from collections import deque`
2. **Edge Case**: Check for `if not root: return []`
3. **Queue Initialization**: `queue = deque([root])`
4. **Level Size Control**: `for _ in range(len(queue)):`
5. **Process Node**: `node = queue.popleft()`
6. **Add Children**: Check left/right and append to queue

### Common Modifications
- **Single values per level**: Change `level.append(node.val)` logic
- **Right-to-left**: Reverse level before appending
- **Special processing**: Add conditions in the processing loop

## Review Problems
- **LeetCode 102**: Binary Tree Level Order Traversal (exact template match)

## 九章
- **CH2**: Binary Tree Level Order Traversal
- **3 Steps:**
- (1) start存queue
- (2) while queue非空
- (3) for loop當前queue, popleft當前node, append下層node
