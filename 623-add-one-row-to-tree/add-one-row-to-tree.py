# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node

        def insert(node, current_depth):
            if not node:
                return
            if current_depth == depth - 1:
                left = node.left
                node.left = TreeNode(val)
                node.left.left = left

                right = node.right
                node.right = TreeNode(val)
                node.right.right = right

            else:
                insert(node.left, current_depth + 1)
                insert(node.right, current_depth + 1)

        insert(root, 1)
        return root
        