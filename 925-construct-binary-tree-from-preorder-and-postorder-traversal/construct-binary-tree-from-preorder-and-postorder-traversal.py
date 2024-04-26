# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None

        d = {val: idx for idx, val in enumerate(postorder)}

        def build_subtree(left, right):
            if left > right:
                return None

            root_val = preorder.pop(0)
            root = TreeNode(root_val)

            if left == right:
                return root

            left_root_idx = d[preorder[0]]

            root.left = build_subtree(left, left_root_idx)
            root.right = build_subtree(left_root_idx + 1, right - 1)

            return root

        return build_subtree(0, len(postorder) - 1)
