# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        steps = 0

        def dfs(node):
            nonlocal steps
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            steps += abs(left) + abs(right)
            return node.val + left + right - 1

        dfs(root)
        return steps
