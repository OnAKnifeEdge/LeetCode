# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([root])
        level = 0

        while q:
            n = len(q)
            pre_val = float('-inf') if level % 2 == 0 else float('inf')
            for _ in range(n):
                node = q.popleft()
                if level % 2 == 0:  # even
                    if node.val % 2 == 0:
                        return False
                    if node.val <= pre_val:
                        return False
                else:  # odd
                    if node.val % 2 != 0:
                        return False
                    if node.val >= pre_val:
                        return False
                pre_val = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return True
