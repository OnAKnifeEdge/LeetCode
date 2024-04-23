# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        parent_x, parent_y = None, None
        d_x, d_y = None, None

        def dfs(node, parent, depth):
            nonlocal parent_x, parent_y, d_x, d_y
            if not node or (d_x and d_y):
                return
            if node.val == x:
                parent_x = parent
                d_x = depth
            elif node.val == y:
                parent_y = parent
                d_y = depth
            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)
        
        dfs(root, None, 0)
        return (d_x == d_y) and (parent_x != parent_y)

        