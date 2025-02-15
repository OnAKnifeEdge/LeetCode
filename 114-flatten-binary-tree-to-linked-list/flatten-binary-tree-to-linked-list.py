# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        left = self.flatten(root.left)
        root.left = None
        right = self.flatten(root.right)
        if not left:
            root.right = right
            return root
        p = left
        while p.right:
            p = p.right
        p.right = right
        root.right = left
        return root
