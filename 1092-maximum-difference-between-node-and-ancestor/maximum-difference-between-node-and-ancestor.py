# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.max_diff = 0

        def dfs(node):
            if not node:
                return float("inf"), float("-inf")
            left_min, left_max = dfs(node.left)
            right_min, right_max = dfs(node.right)
            current_min = min(left_min, node.val, right_min)
            current_max = max(left_max, node.val, right_max)
            self.max_diff = max(
                self.max_diff, abs(node.val - current_min), abs(current_max - node.val)
            )
            return current_min, current_max

        dfs(root)
        return self.max_diff
