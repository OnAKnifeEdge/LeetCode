# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def traverse(node, path=[]):
            if node is None:
                return

            path.append(str(node.val))
            if node.left is None and node.right is None:
                paths.append('->'.join(path))
            else:
                traverse(node.left, path)
                traverse(node.right, path)
            path.pop()

        traverse(root)
        return paths
