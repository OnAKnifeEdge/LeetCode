# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if root is None:
            return None
        if root.val == target:
            return root.val
        if root.val < target:
            candidate = self.closestValue(root.right, target)
            if candidate is None:
                return root.val

            if abs(candidate - target) < abs(root.val - target):
                return candidate
            else:
                return root.val

        candidate = self.closestValue(root.left, target)
        if candidate is None:
            return root.val

        if abs(candidate - target) <= abs(root.val - target):
            return candidate
        else:
            return root.val
