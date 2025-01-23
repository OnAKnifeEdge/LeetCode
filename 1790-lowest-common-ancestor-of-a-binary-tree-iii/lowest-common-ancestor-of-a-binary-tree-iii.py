"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        p_pointer, q_pointer = p, q
        while p_pointer != q_pointer:
            p_pointer = p_pointer.parent if p_pointer else q
            q_pointer = q_pointer.parent if q_pointer else p

        return p_pointer
