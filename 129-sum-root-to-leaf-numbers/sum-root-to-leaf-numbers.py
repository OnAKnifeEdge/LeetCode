# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s = 0
        def dfs(root, current):
            nonlocal s
            if not root:
                return
            current = current * 10 + root.val
            if not root.left and not root.right:
                s += current
            else:
                dfs(root.left, current)
                dfs(root.right, current)
        dfs(root, 0)
        return s

        