# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        bl = root.val if root else None

        def dfs(node, depth):
            nonlocal max_depth, bl
            if not node:
                return
            if depth > max_depth:
                max_depth = depth
                bl = node.val

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return bl

            
        