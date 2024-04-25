# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], t: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == t
        return self.hasPathSum(root.left, t - root.val) or self.hasPathSum(root.right, t - root.val)