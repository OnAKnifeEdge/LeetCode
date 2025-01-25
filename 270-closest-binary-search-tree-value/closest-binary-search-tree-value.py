# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val

        def dfs(node):
            if node is None:
                return
            if node.val < target:
                dfs(node.right)
            else:
                dfs(node.left)

            nonlocal closest
            if abs(node.val - target) < abs(closest - target):
                closest = node.val
            elif abs(node.val - target) == abs(closest - target):
                closest = min(closest, node.val)

        dfs(root)
        return closest
