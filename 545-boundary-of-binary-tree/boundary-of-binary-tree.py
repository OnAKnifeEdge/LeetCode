# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        boundary = [root.val]

        def is_leaf(node):
            return not node.left and not node.right

        def get_left_boundary(node):  # pre-order
            if not node or is_leaf(node):
                return
            if node.left:
                boundary.append(node.val)
                get_left_boundary(node.left)
            elif node.right:
                boundary.append(node.val)
                get_left_boundary(node.right)

        def get_leaves(node):
            if not node:
                return
            if not node.left and not node.right and node != root:
                boundary.append(node.val)
            get_leaves(node.left)
            get_leaves(node.right)

        def get_right_boundary(node):  # post-order
            if not node or is_leaf(node):
                return
            if node.right:
                get_right_boundary(node.right)
                boundary.append(node.val)
            elif node.left:
                get_right_boundary(node.left)
                boundary.append(node.val)


        get_left_boundary(root.left)
        get_leaves(root)
        get_right_boundary(root.right)

        return boundary
