# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)


        def lca(root, nodes):
            if root is None:
                return None
            if root in nodes:
                return root
            left = lca(root.left, nodes)
            right = lca(root.right, nodes)
            if left and right:
                return root
            return left or right
        
        return lca(root, nodes)
        