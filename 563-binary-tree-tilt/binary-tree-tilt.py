# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        s = 0

        def sum_of_tree(node: Optional[TreeNode]) -> int:
            nonlocal s
            if not node:
                return 0
            left = sum_of_tree(node.left)
            right = sum_of_tree(node.right)
            tilt = abs(right - left)
            s += tilt
            return left + node.val + right
        sum_of_tree(root)
        return s
