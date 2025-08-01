# method 1: Ancestor Set

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Store all ancestors of node p in a set
        ancestors = set()
        while p:
            ancestors.add(p)
            p = p.parent

        # Traverse upward from q until we find a common ancestor
        while q:
            if q in ancestors:
                return q  # First common ancestor found
            q = q.parent
        
        return None  # This should not happen in a valid tree


# method 2: two pointers

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Initialize two pointers
        a, b = p, q
        
        # Move both pointers upward
        # When one pointer reaches the root (None),
        # redirect it to the other node's starting point
        while a != b:
            a = a.parent if a else q
            b = b.parent if b else p
        
        # Both pointers meet at the Lowest Common Ancestor (LCA)
        return a
