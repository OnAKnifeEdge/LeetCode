class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:

        def lca(node):
            if not node:
                return
            if node.val == startValue or node.val == destValue:
                return node
            left = lca(node.left)
            right = lca(node.right)
            if left and right:
                return node
            return left if left else right

        lca_node = lca(root)

        def build_path(node, target, path):  # from target to node
            if not node:
                return False
            if node.val == target:
                return True
            if build_path(node.left, target, path):
                path.append("L")
                return True
            if build_path(node.right, target, path):
                path.append("R")
                return True
            return False

        start_to_node = []
        build_path(lca_node, startValue, start_to_node)

        end_to_node = []
        build_path(lca_node, destValue, end_to_node)

        return len(start_to_node) * "U" + "".join(reversed(end_to_node))
