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
            nonlocal closest

            if not node:
                return
            
            if target > node.val:
                dfs(node.right)
            else:
                dfs(node.left)

            if abs(node.val - target) == abs(closest - target):
                closest = min(node.val, closest)
            elif abs(node.val - target) < abs(closest - target):
                closest = node.val

        dfs(root)
        return closest
           