# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        d = {}
        width = 0 

        def dfs(node, depth, idx):
            nonlocal width
            if not node:
                return

            if depth not in d:
                d[depth] = idx

            width = max(width, idx - d[depth] + 1)

            dfs(node.left, depth + 1, 2 * idx)
            dfs(node.right, depth + 1, 2 * idx + 1)

        dfs(root, 0, 0)
        return width
        