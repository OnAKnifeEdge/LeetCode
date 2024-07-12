# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False

        def dfs(node):
            leaves = []
            if not node:
                return []
            if not node.left and not node.right:
                leaves.append(node.val)
            left = dfs(node.left)
            leaves.extend(left)
            right = dfs(node.right)
            leaves.extend(right)
            return leaves

        return dfs(root1) == dfs(root2)
