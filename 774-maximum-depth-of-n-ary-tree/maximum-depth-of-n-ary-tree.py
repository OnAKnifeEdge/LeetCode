"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if root is None:
            return 0
        sub_max_depth = 0
        for node in root.children:
            sub_max_depth = max(sub_max_depth, self.maxDepth(node))
        return sub_max_depth + 1
