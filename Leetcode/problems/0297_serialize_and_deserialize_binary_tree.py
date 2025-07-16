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
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                return ['#']  # Use '#' to represent null nodes
            # Serialize current node, then left and right subtrees
            return [str(node.val)] + dfs(node.left) + dfs(node.right)

        return ','.join(dfs(root))  # Join all values into a comma-separated string

    def deserialize(self, data):
        """
        Decodes the serialized string back to the original binary tree structure.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')  # Split the string into a list of values
        self.i = 0              # Index pointer for recursive traversal

        def dfs():
            if vals[self.i] == '#':
                self.i += 1
                return None  # Return None for null nodes
            
            # Create a new node from the current value
            node = TreeNode(int(vals[self.i]))
            self.i += 1

            # Recursively build left and right subtrees
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
