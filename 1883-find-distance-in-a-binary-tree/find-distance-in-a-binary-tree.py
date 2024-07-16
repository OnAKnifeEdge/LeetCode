# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        if p == q:
            return 0
        result = -1

        def dfs(node: TreeNode) -> int:

            # -1 if neither p nor q is found in the current subtree
            # 0 if the current node is p or q
            # A positive integer representing the distance
            #   from the current node to either p or q if one is found in its subtree

            nonlocal result
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            if node.val == p or node.val == q:
                # Found either p or q, but neither is a descendant of the current node.
                if left < 0 and right < 0:
                    # "I am one of the target nodes, but I don't have the other target in my subtrees".
                    return 0
                # Found either p or q, and the current node is also the LCA.
                result = 1 + (left if left >= 0 else right)
                return -1  # Stop further search

            # Current node is neither p or q, but it is the LCA.
            if left >= 0 and right >= 0:
                result = left + right + 2
                return -1  # Stop further search

            # Continue the search if either p or q is found in the subtrees.
            if left >= 0:
                return left + 1
            if right >= 0:
                return right + 1

            # Neither p or q is found in the subtrees, continue the search.
            return -1

        dfs(root)
        return result
