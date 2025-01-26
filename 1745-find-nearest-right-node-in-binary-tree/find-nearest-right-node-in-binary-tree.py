# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        self.target_depth = None
        self.target_node = None

        def dfs(node, depth):
            if not node:
                return
            if self.target_node:
                return
            if depth == self.target_depth:
                self.target_node = node
                return
            if node.val == u.val:
                self.target_depth = depth
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)


        dfs(root, 0)
        return self.target_node
