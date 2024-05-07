# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        # looking for the first element greater than root_val
        right_idx = len(preorder)
        for idx in range(1, len(preorder)):
            if preorder[idx] < root_val:
                continue
            right_idx = idx
            break
        root.left = self.bstFromPreorder(preorder[1:right_idx])
        root.right = self.bstFromPreorder(preorder[right_idx:])
        return root
