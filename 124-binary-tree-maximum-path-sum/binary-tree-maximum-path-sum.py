# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        s = float("-inf")

        def findMaxPath(node: Optional[TreeNode]) -> int:
            nonlocal s
            if not node:
                return 0
            left = max(findMaxPath(node.left), 0)
            right = max(findMaxPath(node.right), 0)
            s = max(left + node.val + right, s)
            return max(left + node.val, right + node.val)

        findMaxPath(root)
        return s
