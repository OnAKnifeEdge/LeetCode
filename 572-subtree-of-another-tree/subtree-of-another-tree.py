# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_same_tree(a, b):
            if not a:
                return not b
            if not b:
                return not a
            if a.val != b.val:
                return False
            return is_same_tree(a.left, b.left) and is_same_tree(a.right, b.right)

        if not root:
            return not subRoot

        if is_same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
