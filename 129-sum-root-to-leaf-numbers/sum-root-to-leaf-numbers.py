# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path_sums = 0

        def traverse(node, path_sum=0, path=[]):
            nonlocal path_sums
            if node is None:
                return
            path_sum = 10 * path_sum + node.val
            path.append(node.val)
            if node.left is None and node.right is None:
                path_sums += path_sum
            else:
                traverse(node.left, path_sum)
                traverse(node.right, path_sum)
            val = path.pop()
            path_sum = (path_sum - val) // 10

        traverse(root)
        return path_sums
