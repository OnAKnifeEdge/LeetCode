# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node, tail):
            if not node:
                return tail
            left = inorder(node.left, node)
            node.left = None
            node.right = inorder(node.right, tail)
            return left
        return inorder(root, None)
