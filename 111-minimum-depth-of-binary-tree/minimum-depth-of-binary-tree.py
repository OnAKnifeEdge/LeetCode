# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([])
        if root is not None:
            q.append(root)
        else:
            return 0
        depth = 1
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
        return depth
