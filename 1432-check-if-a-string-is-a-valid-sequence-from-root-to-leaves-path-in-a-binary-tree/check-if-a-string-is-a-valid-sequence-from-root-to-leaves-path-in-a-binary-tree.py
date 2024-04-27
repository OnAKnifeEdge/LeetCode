# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:

        def check(node, i):
            if not node and arr:
                return False
            if i == len(arr):
                return False
            if arr[i] != node.val:
                return False
            if not node.left and not node.right:
                return i == len(arr) - 1
            return check(node.left, i + 1) or check(node.right, i + 1)

        return check(root, 0)
