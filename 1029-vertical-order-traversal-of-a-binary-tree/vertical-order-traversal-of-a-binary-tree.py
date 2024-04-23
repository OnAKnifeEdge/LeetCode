# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    class Position(NamedTuple):
        val: int
        row: int
        col: int

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        self.nodes = []

        def traverse(node, row, col):
            if not node:
                return
            self.nodes.append(self.Position(val=node.val, row=row, col=col))
            traverse(node.left, row + 1, col - 1)
            traverse(node.right, row + 1, col + 1)

        traverse(root, 0, 0)
        self.nodes.sort(key = lambda x: (x.col, x.row, x.val))


        column_map = defaultdict(list)
        min_col, max_col = 0, 0  # Initializing to track the range of columns.

        for node in self.nodes:
            column_map[node.col].append(node.val)
            min_col = min(min_col, node.col)  # Update the minimum column.
            max_col = max(max_col, node.col)  # Update the maximum column.

        # Build the result by iterating over the computed range.
        result = [column_map[col] for col in range(min_col, max_col + 1)]

        return result

        return result

        
