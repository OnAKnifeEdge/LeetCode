# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        count = 0 

        def dfs(node):
            nonlocal count
            if not node:
                return True
            
            is_left_uni = dfs(node.left)
            is_right_uni = dfs(node.right)

            if is_left_uni and is_right_uni:
                if node.left and node.val != node.left.val:
                    return False
                if node.right and node.val != node.right.val:
                    return False
                count += 1
                return True
            return False
        dfs(root)
        return count
        