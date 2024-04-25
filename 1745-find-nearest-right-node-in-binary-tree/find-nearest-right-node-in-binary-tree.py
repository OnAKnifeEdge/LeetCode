# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        target_depth = None
        result = None

        def dfs(node, depth):
            nonlocal target_depth, result
            if not node or result:
                return
            if node.val == u.val:
                target_depth = depth
            elif depth == target_depth:
                result = node
                return
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
        dfs(root, 0)
        return result

        