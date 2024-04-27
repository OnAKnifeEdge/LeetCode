# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def max_length(node):
            nonlocal balanced
            if not node:
                return 0
            left_length = max_length(node.left)
            right_length = max_length(node.right)

            if abs(left_length - right_length) > 1:
                balanced = False

            return 1 + max(left_length, right_length)

        max_length(root)
        return balanced
