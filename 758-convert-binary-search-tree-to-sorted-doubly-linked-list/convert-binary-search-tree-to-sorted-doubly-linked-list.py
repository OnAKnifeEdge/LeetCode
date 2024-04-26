"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

# left： prev
# right: next


class Solution:
    def treeToDoublyList(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return None

        left_head = self.treeToDoublyList(root.left)
        right_head = self.treeToDoublyList(root.right)

        # Connect root with its left subtree (if it exists)
        if left_head:
            left_tail = left_head.left  # left_head 前一个是 left_tail
            left_tail.right = root  # left_tail 下一个是 root
            root.left = left_tail  # root 前一个是 left_tail
        else:
            left_head = root  # If no left subtree, root itself is the smallest element

        # Connect root with its right subtree (if it exists)
        if right_head:
            right_tail = right_head.left
            right_head.left = root  # right_head 前一个是 root
            root.right = right_head  # root 下一个是 right_head
        else:
            right_tail = root  # If no right subtree, root itself is the biggest element

        # Make the list circular by connecting the heads and tails
        left_head.left = right_tail
        right_tail.right = left_head

        return left_head
