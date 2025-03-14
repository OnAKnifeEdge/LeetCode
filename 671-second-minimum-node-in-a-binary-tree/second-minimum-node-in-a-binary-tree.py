# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        min1 = root.val
        min2 = float("inf")
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == min1:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            elif node.val > min1:
                min2 = min(min2, node.val)
        return min2 if min2 != float("inf") else -1
