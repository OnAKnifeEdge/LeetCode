# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def get_height(node):
            if not node:
                return 0, True
            left_height, left_is_balanced = get_height(node.left)
            right_height, right_is_balanced = get_height(node.right)
            height = max(left_height, right_height) + 1
            if abs(left_height - right_height) > 1:
                return height, False
            if not left_is_balanced or not right_is_balanced:
                return height, False
            return height, True

        if not root:
            return True

        _, balanced = get_height(root)
        return balanced