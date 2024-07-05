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
        if root is None:
            return None
        if root == p or root == q:
            return root
        # The result or right can be one of three things:

        # The node where we find either p or q, if one of them is in the left subtree.
        # The LCA of p and q, if both are in the left subtree.
        # None, if neither p nor q is in the left subtree.

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right
