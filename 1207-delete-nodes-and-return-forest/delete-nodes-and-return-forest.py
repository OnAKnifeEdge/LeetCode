# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        to_delete = set(to_delete)
        forests = []

        def delete(node, has_parent):
            if not node:
                return None
            keep = True
            if node.val in to_delete:
                keep = False
            if keep and not has_parent:
                forests.append(node)
            node.left = delete(node.left, keep)
            node.right = delete(node.right, keep)
            if keep:
                return node
            else:
                return None

        delete(root, False)
        return forests