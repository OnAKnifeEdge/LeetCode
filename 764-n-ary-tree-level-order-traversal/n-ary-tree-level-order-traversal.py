"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if root is None:
            return []
        q = deque([root])
        level_order = []
        while q:
            n = len(q)
            level = []
            for i in range(n):
                node = q.popleft()
                level.append(node.val)
                if i == n - 1:
                    level_order.append(level)
                q.extend(node.children)
        return level_order
