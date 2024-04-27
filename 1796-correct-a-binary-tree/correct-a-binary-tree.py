# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        visited = set()

        def correct(node):
            if not node:
                return None
            if node.right and node.right in visited:
                return None
            visited.add(node)
            node.right = correct(node.right)
            node.left = correct(node.left)
            return node
        return correct(root)
