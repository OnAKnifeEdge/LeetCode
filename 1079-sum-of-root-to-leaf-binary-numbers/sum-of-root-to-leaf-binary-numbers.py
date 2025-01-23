# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        s = 0

        def dfs(node, current):
            if node is None:
                return
            nonlocal s
            current = current * 2 + node.val
            if node.left is None and node.right is None:
                s += current
            dfs(node.left, current)
            dfs(node.right, current)

        dfs(root, 0)
        return s
