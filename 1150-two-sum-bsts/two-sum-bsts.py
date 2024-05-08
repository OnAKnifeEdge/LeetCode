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

        needs = set()

        def fill_needs(node):
            if not node:
                return
            fill_needs(node.left)
            needs.add(target - node.val)
            fill_needs(node.right)

        fill_needs(root1)

        # find if any value in root2 tree is in needs

        def check_need(node):
            if not node:
                return False
            if node.val in needs:
                return True
            return check_need(node.left) or check_need(node.right)

        return check_need(root2)

    def twoSumBSTsTwoPointers(
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

        while i < len(arr1) and j >= 0:
            if arr1[i] + arr2[j] > target:
                j -= 1
            elif arr1[i] + arr2[j] < target:
                i += 1
            else:
                return True
        return False
