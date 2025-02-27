# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return 0, node
            left_depth, left = dfs(node.left)
            right_depth, right = dfs(node.right)
            if left_depth > right_depth:
                return left_depth + 1, left
            if right_depth > left_depth:
                return right_depth + 1, right
            return left_depth + 1, node

        _, node = dfs(root)
        return node
