# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            nonlocal count
            if not node:
                return
            path = path ^ (1 << node.val)

            if not node.left and not node.right:
                if path & (path - 1) == 0:
                    count += 1
            else:
                dfs(node.left, path)
                dfs(node.right, path)
        count = 0
        dfs(root, 0)
        return count        