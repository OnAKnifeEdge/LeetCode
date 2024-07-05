# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", nodes: "List[TreeNode]"
    ) -> "TreeNode":
        nodes = set(nodes)

        def lca(node, nodes):
            if node is None:
                return None
            if node in nodes:
                return node
            left = lca(node.left, nodes)
            right = lca(node.right, nodes)

            if left and right:
                return node

            return left or right

        return lca(root, nodes)
