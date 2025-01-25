# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        nodes = defaultdict(list)
        result = []
        max_col, min_col = 0, 0

        def dfs(col, row, node):
            if not node:
                return
            nonlocal max_col, min_col
            nodes[col].append((row, node.val))
            max_col = max(max_col, col)
            min_col = min(min_col, col)
            dfs(col - 1, row + 1, node.left)
            dfs(col + 1, row + 1, node.right)

        dfs(0, 0, root)

        for col in range(min_col, max_col + 1):
            result.append([val for _, val in sorted(nodes[col])])
        return result
