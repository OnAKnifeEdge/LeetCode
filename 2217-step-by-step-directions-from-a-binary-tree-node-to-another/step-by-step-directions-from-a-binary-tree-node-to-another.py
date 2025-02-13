# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:

        def find_lca(node, startValue, destValue):
            if not node:
                return None
            if node.val == startValue or node.val == destValue:
                return node
            left = find_lca(node.left, startValue, destValue)
            right = find_lca(node.right, startValue, destValue)
            if left and right:
                return node
            return left or right

        def build_path(lca, val, path):  # from val to lca
            if not lca:
                return False
            if lca.val == val:
                return True
            if build_path(lca.left, val, path):
                path.append("L")
                return True
            if build_path(lca.right, val, path):
                path.append("R")
                return True

        lca = find_lca(root, startValue, destValue)
        path = []
        start_to_lca, end_to_lca = [], []
        build_path(lca, startValue, start_to_lca)

        path.extend("U" * len(start_to_lca))
        build_path(lca, destValue, end_to_lca)

        path.extend(list(reversed(end_to_lca)))
        return ''.join(path)
