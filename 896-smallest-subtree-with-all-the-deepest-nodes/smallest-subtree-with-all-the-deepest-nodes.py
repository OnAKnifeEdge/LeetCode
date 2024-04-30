# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        def dfs(node: Optional[TreeNode]) -> Tuple[int, Optional[TreeNode]]:
            # depth and it's LCA containing the lowest leaves
            if not node:
                return 0, None
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)
            if left_depth == right_depth:
                return left_depth + 1, node
            if left_depth > right_depth:
                return left_depth + 1, left_lca
            return right_depth + 1, right_lca

        return dfs(root)[1]
