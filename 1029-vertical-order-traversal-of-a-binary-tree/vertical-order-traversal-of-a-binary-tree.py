# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        self.d = defaultdict(list)
        self.min = 0
        self.max = 0

        def traverse(node, row, col):
            if not node:
                return
            self.d[col].append((row, node.val))
            self.min = min(col, self.min)
            self.max = max(col, self.max)
            traverse(node.left, row + 1, col - 1)
            traverse(node.right, row + 1, col + 1)

        traverse(root, 0, 0)

        # Build the result by iterating over the computed range.

        result = []
        for col in range(self.min, self.max + 1):
            # sort first by 'row', then by 'value', in ascending order using a lambda function as the sort key
            result.append([val for row, val in sorted(self.d[col])])

        return result



        
