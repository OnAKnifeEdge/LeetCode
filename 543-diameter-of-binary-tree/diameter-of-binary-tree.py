# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def max_depth(node: Optional[TreeNode]):

            if node is None:
                return 0
            left = max_depth(node.left)
            right = max_depth(node.right)
            self.diameter = max(left + right, self.diameter)
            return max(left, right) + 1
        max_depth(root)
        return self.diameter
        