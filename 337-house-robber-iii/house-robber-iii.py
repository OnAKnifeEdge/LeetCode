# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dp(node):
            if not node:
                return 0, 0
            rob_left_yes, rob_left_no = dp(node.left)
            rob_right_yes, rob_right_no = dp(node.right)
            rob_node_yes = node.val + rob_left_no + rob_right_no
            rob_node_no = max(rob_left_yes, rob_left_no) + max(
                rob_right_yes, rob_right_no
            )
            return rob_node_yes, rob_node_no

        return max(dp(root))
