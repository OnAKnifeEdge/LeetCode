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
        val1, val2 = min(p.val, q.val), max(p.val, q.val)

        while root:
            if root.val < val1:
                root = root.right
            elif root.val > val2:
                root = root.left
            else:
                return root
