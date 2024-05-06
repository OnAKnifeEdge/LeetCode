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
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root or not root.left:
            return root

        def traverse(left, right):
            if not left or not right:
                return
            left.next = right
            traverse(left.left, left.right)
            traverse(left.right, right.left)
            traverse(right.left, right.right)

        traverse(root.left, root.right)
        return root
