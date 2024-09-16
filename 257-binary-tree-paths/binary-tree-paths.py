# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        stack = [(root, str(root.val))] # node, path
        result = []
        while stack:
            node, path = stack.pop()
            if node.left is None and node.right is None: # if leaf
                result.append(path)
            if node.left is not None:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right is not None:
                stack.append((node.right, path + '->' + str(node.right.val)))
        return result

        