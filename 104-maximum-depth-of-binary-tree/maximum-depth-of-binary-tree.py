# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [(root, 1)]
        max_depth = 1
        while stack:
            node, d = stack.pop()
            if node.left:
                stack.append((node.left, d + 1))
            if node.right:
                stack.append((node.right, d + 1))
            max_depth = max(d, max_depth)
        return max_depth
