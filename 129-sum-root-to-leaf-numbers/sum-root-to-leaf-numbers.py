# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def traverse(root, n):
            nonlocal s
            if not root:
                return
            n = n * 10 + root.val
            if not root.left and not root.right:
                s += n
            traverse(root.left, n)
            traverse(root.right, n)
        s = 0
        traverse(root, 0)
        return s
        