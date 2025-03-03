"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        if root.left and root.right: 
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        left = self.connect(root.left)
        right = self.connect(root.right)
        root.left = left
        root.right = right
        return root

        