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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque([root])
        while q:
            n = len(q)
            pre = None
            for i in range(n):
                current = q.popleft()
                if pre:
                    pre.next = current
                pre = current
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
        return root

        