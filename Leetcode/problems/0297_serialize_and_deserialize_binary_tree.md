# Leetcode 0297 - Serialize and Deserialize Binary Tree

## ☀️ UMPIRE

- **Understand**: Convert a binary tree into a string and back. Use '#' to represent null nodes.
- **Match**: Binary Tree + recursion pattern. Best suited for DFS traversal.
- **Plan**: Use preorder traversal (node-left-right). Serialize by joining values with commas. Deserialize by reading one value at a time and rebuilding the tree recursively.
- **Implement**: See below.
- **Review**: Ensure null nodes are represented, and index tracking is correctly handled.
- **Evaluate**: Time O(n) for both serialization and deserialization, where n is the number of nodes. Space O(n) due to recursion stack and the output list.

---

## ☀️ Metadata

- **Appears In**: Grind75
- **Pattern**: DFS Tree Recursion
- **Data Structure**: Binary Tree
- **Algorithm**: DFS, Recursion
- **Tags**: Tree, DFS, Serialization, Recursion

---

## ☀️ Solution Code

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """
        Encodes a binary tree to a single string using preorder traversal.
        """
        def dfs(node):
            if not node:
                return ['#']  # Use '#' to represent null nodes
            return [str(node.val)] + dfs(node.left) + dfs(node.right)

        return ','.join(dfs(root))

    def deserialize(self, data):
        """
        Decodes the serialized string back to the original binary tree structure.
        """
        vals = data.split(',')  # Split the string into a list of values
        self.i = 0              # Index pointer for recursive traversal

        def dfs():
            if vals[self.i] == '#':
                self.i += 1
                return None  # Return None for null nodes

            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
```

---

## ☀️ Trace

```
Input: "1,2,#,#,3,#,#"

deserialize() steps:
- i=0: '1' -> create TreeNode(1)
- i=1: '2' -> create TreeNode(2)
- i=2: '#' -> left of 2 is None
- i=3: '#' -> right of 2 is None
- i=4: '3' -> create TreeNode(3)
- i=5: '#' -> left of 3 is None
- i=6: '#' -> right of 3 is None
- Return root: TreeNode(1)
```

---

## ☀️ Line-by-line Typing Script

- I’m defining the Codec class with two methods: serialize and deserialize.
- In serialize, I define a helper dfs function that traverses the tree using preorder.
- If the current node is None, I return ['#'] to mark it as a null node.
- Otherwise, I convert the node value to a string, then recursively call dfs on the left and right children.
- After building a list of strings, I use ','.join() to convert it into one single string.
- In deserialize, I split the input string by ',' to get the values list.
- I use self.i to track the current index as I traverse the list.
- In the dfs function, if the current value is '#', I return None and move to the next index.
- Otherwise, I create a new TreeNode with the current value.
- I then recursively build the left and right subtrees.
- Finally, I return the constructed node and complete the tree.

```
