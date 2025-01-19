# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {v: i for i, v in enumerate(inorder)}

        def build(postorder_start, postorder_end, inorder_start, inorder_end):
            if inorder_start > inorder_end:
                return
            root_val = postorder[postorder_end]
            root = TreeNode(root_val)
            inorder_root_idx = inorder_map[root_val]
            left_size = inorder_root_idx - inorder_start
            

            root.left = build(
                postorder_start,
                postorder_start + left_size - 1,
                inorder_start,
                inorder_root_idx - 1,
            )

            root.right = build(
                postorder_start + left_size,
                postorder_end - 1,
                inorder_root_idx + 1,
                inorder_end,
            )
            return root

        return build(0, len(inorder) - 1, 0, len(inorder) - 1)