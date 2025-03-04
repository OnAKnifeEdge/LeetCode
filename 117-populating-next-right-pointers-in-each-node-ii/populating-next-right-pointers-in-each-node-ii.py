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
    def connect(self, root: "Node") -> "Node":
        if not root:
            return
        q = deque([root])
        while q:
            n = len(q)
            pointer = None
            for _ in range(n):
                node = q.popleft()
                if pointer:
                    pointer.next = node
                pointer = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root
