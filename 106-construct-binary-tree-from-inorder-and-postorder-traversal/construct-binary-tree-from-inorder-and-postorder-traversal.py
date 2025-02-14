# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {v: idx for idx, v in enumerate(inorder)}

        def build(postorder_end, inorder_start, inorder_end):

            # root is at post_end.

            # right subtree's root is at post_end -1.

            # left subtree's root is at post_end - right_size - 1
            # right_size is the size of the right subtree (in_end - in_root_idx).

            if inorder_start > inorder_end:
                return None
            root_val = postorder[postorder_end]
            inorder_root_idx = inorder_map[root_val]
            right_side = inorder_end - inorder_root_idx
            root = TreeNode(root_val)
            root.right = build(postorder_end - 1, inorder_root_idx + 1, inorder_end)
            root.left = build(postorder_end - 1 - right_side, inorder_start, inorder_root_idx - 1)
            return root

        return build(len(postorder) - 1, 0, len(postorder) - 1)
