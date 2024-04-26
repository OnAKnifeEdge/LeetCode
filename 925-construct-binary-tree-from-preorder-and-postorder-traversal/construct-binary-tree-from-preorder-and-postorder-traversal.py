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
        d = {val: idx for idx, val in enumerate(postorder)}  # {val: idx} for preorder

        def build(start, end):
            if start > end:
                return None

            root_val = preorder.pop(0)
            root = TreeNode(root_val)

            if start == end:
                return root

            left_root_val = preorder[0]
            left_root_idx = d[left_root_val]

            root.left = build(start, left_root_idx)
            root.right = build(left_root_idx + 1, end - 1)
            return root

        return build(0, len(preorder) - 1)
