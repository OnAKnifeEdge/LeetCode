# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_same_tree(p1, p2):
            if not p1 and not p2:
                return True
            if not p1 or not p2:
                return False
            if p1.val != p2.val:
                return False
            return is_same_tree(p1.left, p2.left) and is_same_tree(p1.right, p2.right)

        if not root and not subRoot:
            return True

        if not root and subRoot:
            return False

        if is_same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
