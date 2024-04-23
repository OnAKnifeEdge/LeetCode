# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        def dfs(node, depth):
            if not node:
                return
            if depth == 1:
                node.left = TreeNode(val, node.left)
                node.right = TreeNode(val, None, node.right)
            else:
                dfs(node.left, depth - 1)
                dfs(node.right, depth - 1)
            return node

        return dfs(TreeNode(0, root), depth).left

        