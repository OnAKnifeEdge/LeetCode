# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        has_p = False
        has_q = False

        def lca(root, p, q):
            nonlocal has_p, has_q  # To modify the outer variables
            if root is None:
                return None
            left = lca(root.left, p, q)
            right = lca(root.right, p, q)

            if left and right:
                return root

            
            if root == p:
                has_p = True
                return root
            if root == q:
                has_q = True
                return root

            # if root.val == p.val or root.val == q.val:
            #     if root.val == p.val:
            #         has_p = True
            #     if root.val == q.val:
            #         has_q = True
            #     return root

            return left or right

        node = lca(root, p, q)
        if not has_p or not has_q:
            return None
        return node
