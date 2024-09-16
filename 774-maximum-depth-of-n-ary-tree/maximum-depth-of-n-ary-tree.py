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
        max_depth = 0
        for child in root.children:
            d = self.maxDepth(child)
            max_depth = max(max_depth, d)
        return max_depth + 1
