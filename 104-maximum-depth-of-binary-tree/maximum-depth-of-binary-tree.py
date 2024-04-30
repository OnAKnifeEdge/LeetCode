# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        d = 0

        def dfs(node) -> int:
            nonlocal d
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left > right:
                d = max(d, left + 1)
                return left + 1

            d = max(d, right + 1)
            return right + 1

        dfs(root)
        return d
