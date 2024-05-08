# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int
    ) -> bool:
        if not root1 or not root2:
            return False

        def inorder(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        arr1, arr2 = inorder(root1), inorder(root2)

        i = 0
        j = len(arr2) - 1

        while i < len(arr1) and j > 0:
            if arr1[i] + arr2[j] > target:
                j -= 1
            elif arr1[i] + arr2[j] < target:
                i += 1
            else:
                return True
        return False
