"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def cloneTree(self, root: "Node") -> "Node":
        if not root:
            return None
        root_copy = Node(val=root.val, children=[])
        for child in root.children:
            root_copy.children.append(self.cloneTree(child))
        return root_copy

