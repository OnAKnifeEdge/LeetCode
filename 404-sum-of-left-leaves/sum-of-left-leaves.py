# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        s = 0

        def dfs(node):
            nonlocal s
            if not node:
                return
            if node.left and not node.left.left and not node.left.right:
                s += node.left.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return s