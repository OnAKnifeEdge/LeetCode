# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path_sums = 0

        def traverse(node, path=[]):
            nonlocal path_sums
            if node is None:
                return
            path.append(str(node.val))
            if node.left is None and node.right is None:
                path_sums += int(''.join(path))
            else:
                traverse(node.left, path)
                traverse(node.right, path)
            path.pop()

        traverse(root)
        return path_sums
