# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        def get_height(node):
            if not node:
                return 0
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            height = max(left_height, right_height) + 1
            if abs(left_height - right_height) > 1:
                self.is_balanced = False
            return height

        if not root:
            return True

        get_height(root)
        return self.is_balanced