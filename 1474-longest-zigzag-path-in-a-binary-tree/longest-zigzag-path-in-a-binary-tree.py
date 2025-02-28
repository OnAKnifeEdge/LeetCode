# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest = 0

        def dfs(node):
            if not node:
                return -1, -1
            _, left_right = dfs(node.left)
            right_left, _ = dfs(node.right)
            left_right += 1
            right_left += 1
            self.longest = max(self.longest, left_right, right_left)
            return left_right, right_left

        dfs(root)
        return self.longest
