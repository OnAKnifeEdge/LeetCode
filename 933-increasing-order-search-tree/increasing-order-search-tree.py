# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        left = self.increasingBST(root.left)
        root.left = None
        right = self.increasingBST(root.right)
        root.right = right
        if not left:
            return root
        p = left
        while p.right:
            p = p.right
        p.right = root
        return left
