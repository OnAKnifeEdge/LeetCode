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
        if not root or not root.left:
            return root
        self.traverse(root.left, root.right)
        return root


    def traverse(self, a: 'Optional[Node]', b: 'Optional[Node]') -> None:
        if not a or not b:
            return
        a.next = b
        self.traverse(a.left, a.right)
        self.traverse(a.right, b.left)
        self.traverse(b.left, b.right)

