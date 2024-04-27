# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        t = None

        def inorder(o, c):
            nonlocal t
            if not o:
                return
            inorder(o.left, c.left)
            if o is target:
                t = c
                return
            inorder(o.right, c.right)

        inorder(original, cloned)
        return t
