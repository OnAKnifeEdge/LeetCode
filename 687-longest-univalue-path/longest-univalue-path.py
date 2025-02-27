# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        self.longest = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            if node.left and node.val == node.left.val:
                left_path = left
            else:
                left_path = 0

            if node.right and node.val == node.right.val:
                right_path = right
            else:
                right_path = 0

            path = left_path + right_path
            self.longest = max(self.longest, path)
            return max(left_path, right_path) + 1

        dfs(root)
        return self.longest
