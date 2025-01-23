# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:

        def find_lca(root, p, q):
            if root is None or root.val == p or root.val == q:
                return root
            left = find_lca(root.left, p, q)
            right = find_lca(root.right, p, q)
            if left and right:
                return root
            return left if left else right

        lca = find_lca(root, p, q)

        def find_distance(root, target, depth):
            if not root:
                return -1
            if root.val == target:
                return depth
            left = find_distance(root.left, target, depth + 1)
            if left != -1:
                return left
            return find_distance(root.right, target, depth + 1)



        return find_distance(lca, p, 0) + find_distance(lca, q, 0)
