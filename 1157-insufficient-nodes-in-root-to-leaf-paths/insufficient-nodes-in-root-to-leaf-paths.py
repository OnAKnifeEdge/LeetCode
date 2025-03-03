# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(
        self, root: Optional[TreeNode], limit: int
    ) -> Optional[TreeNode]:
        if not root:
            return None
        if not root.left and not root.right:
            if root.val < limit:
                return None
            else:
                return root
        left = self.sufficientSubset(root.left, limit - root.val)
        right = self.sufficientSubset(root.right, limit - root.val)
        if not left and not right:
            return None
        root.left = left
        root.right = right
        return root
