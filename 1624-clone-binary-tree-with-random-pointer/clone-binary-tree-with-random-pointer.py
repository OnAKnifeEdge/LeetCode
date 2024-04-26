# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random


class Solution:
    def copyRandomBinaryTree(self, root: "Optional[Node]") -> "Optional[NodeCopy]":
        d = {}

        def copy(node):
            if not node:
                return None
            if node in d:
                return d[node]
            node_copy = NodeCopy(node.val)
            d[node] = node_copy
            node_copy.left = copy(node.left)
            node_copy.right = copy(node.right)
            node_copy.random = copy(node.random)
            return node_copy

        return copy(root)
