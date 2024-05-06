# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([root])
        # If we find any 'not-none' node after this spot, the tree isn't complete.
        found_empty = False

        while q:
            node = q.popleft()
            if not node:
                found_empty = True
            # found a 'not-none' node
            else:
                if found_empty:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True

