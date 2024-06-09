# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float("-inf")

        def get_max_path_sum(node):
            nonlocal max_path_sum
            if not node:
                return 0
            left = max(get_max_path_sum(node.left), 0)
            right = max(get_max_path_sum(node.right), 0)
            max_path_sum = max(max_path_sum, left + right + node.val)
            return max(left + node.val, right + node.val)

        get_max_path_sum(root)
        return max_path_sum
