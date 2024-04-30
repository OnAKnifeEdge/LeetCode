# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        diff = 0

        def dfs(node) -> Tuple[int, int]:
            nonlocal diff
            if not node:
                return float("inf"), float("-inf")
            left_min, left_max = dfs(node.left)
            right_min, right_max = dfs(node.right)
            # Current values to compare with.
            current_min = min(left_min, right_min, node.val)
            current_max = max(left_max, right_max, node.val)
            diff = max(diff, abs(node.val - current_min), abs(current_max - node.val))

            return current_min, current_max

        dfs(root)
        return diff
