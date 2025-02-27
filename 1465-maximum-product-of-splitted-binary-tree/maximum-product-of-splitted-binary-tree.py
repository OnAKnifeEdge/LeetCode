# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.product = 0
        self.MOD = 10**9 + 7

        def get_sum(node):
            if not node:
                return 0
            left = get_sum(node.left)
            right = get_sum(node.right)
            return left + right + node.val

        self.total = get_sum(root)

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            val = left + right + node.val
            p = val * (self.total - val)
            self.product = max(self.product, p)
            return val

        dfs(root)
        return self.product % self.MOD
