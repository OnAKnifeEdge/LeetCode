# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p

        def lca(root, p, q):
            if not root:
                return None
            if root.val > q.val:
                return lca(root.left, p, q)
            if root.val < p.val:
                return lca(root.right, p, q)
            return root

        return lca(root, p, q)

        
        