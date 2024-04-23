# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:

        if depth == 1:
            return TreeNode(val, left=root)

        def dfs(node, d):
            if not node:
                return
            # if we're currently at the nodes directly above where the new row should be.
            if depth - 1 == d:
                node.left = TreeNode(val, left=node.left)
                node.right = TreeNode(val, right=node.right)
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)

        dfs(root, 1)
        return root
