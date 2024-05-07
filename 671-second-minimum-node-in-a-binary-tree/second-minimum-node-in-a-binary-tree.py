# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        if not root.left and not root.right:
            return -1
        left, right = root.left.val, root.right.val
        if root.left.val == root.val:
            left = self.findSecondMinimumValue(root.left)
        if root.right.val == root.val:
            right = self.findSecondMinimumValue(root.right)
        if left == -1:
            return right
        if right == -1:
            return left
        return min(left, right)
