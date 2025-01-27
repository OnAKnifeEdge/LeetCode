# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.result = root.val if root else None
        self.max_level = 0

        def dfs(node, level):
            if not node:
                return
            level += 1
            if level > self.max_level:
                self.result = node.val
                self.max_level = level
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return self.result
