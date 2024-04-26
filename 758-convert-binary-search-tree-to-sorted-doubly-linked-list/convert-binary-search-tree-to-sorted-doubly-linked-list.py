"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: "Optional[Node]") -> "Optional[Node]":

        def helper(node):
            head, tail = node, node

            if node.left:
                head_left, tail_left = helper(node.left)
                head = head_left

                # tail_left <-> node
                tail_left.right = node
                node.left = tail_left

            if node.right:
                head_right, tail_right = helper(node.right)
                tail = tail_right

                # node <-> head_right
                head_right.left = node
                node.right = head_right

            # connect head and tail
            head.left = tail
            tail.right = head
            return head, tail

        if not root:
            return None
        else:
            head, tail = helper(root)
            return head
