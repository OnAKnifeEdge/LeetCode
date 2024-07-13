# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def dfs(node, left, right):
            nonlocal longest
            if not node:
                return
            longest = max(longest, left, right)
            if node.right:
                dfs(node.right, 0, left + 1)
            if node.left:
                dfs(node.left, right + 1, 0)

        dfs(root, 0, 0)
        return longest
