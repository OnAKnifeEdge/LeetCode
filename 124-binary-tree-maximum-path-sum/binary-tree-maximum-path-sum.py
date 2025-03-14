# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float("-inf")

        def max_path(node):
            if not node:
                return 0
            left = max(max_path(node.left), 0)
            right = max(max_path(node.right), 0)
            self.max_path_sum = max(left + right + node.val, self.max_path_sum)
            return max(node.val + left, node.val + right)

        max_path(root)
        return self.max_path_sum
