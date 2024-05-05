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

            # After adjusting the subtree rooted at the current node, 
            # this line calculates the net excess or deficit of coins
            # taking into account the current node's initial coins, 
            # adjustments made in its subtrees, and ensuring it itself ends up with one coin.

            return node.val + left + right - 1

        dfs(root)
        return steps
