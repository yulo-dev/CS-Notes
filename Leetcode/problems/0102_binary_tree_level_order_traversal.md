# Leetcode 0102 - Binary Tree Level Order Traversal

## ☀️ UMPIRE

- **Understand**:  
  Given the root of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).
- **Match**:  
  This is a binary tree traversal problem. We need to return a 2D list based on level grouping → use **Breadth-First Search (BFS)**.
- **Plan**:  
  Use a queue to implement BFS. For each level:
  - Record the number of nodes (`level_size`)
  - Iterate over this count
  - Pop from queue, collect `.val`, and append `.left` / `.right` into queue
- **Review**:  
  Confirm each level is isolated correctly  
  Queue grows and shrinks properly between levels  
  Each `level` only contains `.val`, not TreeNode objects
- **Evaluate**:  
  - Time: O(n), since each node is visited once  
  - Space: O(n), due to the queue and the result list

## ☀️ Metadata

- **Appears In**: Grind75  
- **Pattern**: BFS traversal  
- **Data Structure**: Binary Tree, Queue  
- **Algorithm**: BFS  
- **Tags**: Tree, BFS, Level Order Traversal

## ☀️ Solution Code

```python
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []  # Empty tree → return empty list

        result = []               # Final list of level values
        queue = deque([root])     # Initialize queue with root node

        while queue:
            level_size = len(queue)  # Number of nodes at current level
            level = []               # Store current level values

            for _ in range(level_size):
                node = queue.popleft()     # Pop from front of queue
                level.append(node.val)     # Add current node's value

                if node.left:
                    queue.append(node.left)   # Enqueue left child
                if node.right:
                    queue.append(node.right)  # Enqueue right child

            result.append(level)  # Add completed level to result

        return result
```

## ☀️ Trace

```
Input Tree:
       1
      / \
     2   3
    / \
   4   5

Step-by-step:

queue = [1]
level_size = 1
→ popleft 1 → level = [1]
→ append 2 and 3 to queue
→ result = [[1]]

queue = [2, 3]
level_size = 2
→ popleft 2 → level = [2]
→ append 4 and 5 to queue
→ popleft 3 → level = [2, 3]
→ result = [[1], [2, 3]]

queue = [4, 5]
level_size = 2
→ popleft 4 → level = [4]
→ popleft 5 → level = [4, 5]
→ result = [[1], [2, 3], [4, 5]]

queue = []
done
```

## ☀️ Line-by-line Typing Script

- I’m defining the `levelOrder` function to return a list of lists representing each level of the tree.
- If the root is None, I return an empty list.
- I initialize a result list to store the final output.
- I use a `deque` queue, starting with the root node.
- While the queue is not empty, I determine how many nodes are in the current level using `len(queue)`.
- I create a `level` list to store node values for this level.
- I loop over the number of nodes at this level.
- For each node, I pop it from the queue, store its `.val` in `level`, and enqueue its left and right children if they exist.
- After the level is processed, I append `level` to `result`.
- After the BFS loop finishes, I return the `result`.
