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

        found_p, found_q = False, False

        def find(node):
            if node is None:
                return
            left = find(node.left)
            right = find(node.right)
            if left and right:
                return node
            nonlocal found_p, found_q
            if node.val == p.val:
                found_p = True
                return node
            if node.val == q.val:
                found_q = True
                return node
            return left or right

        possible_lca = find(root)
        return possible_lca if found_p and found_q else None
