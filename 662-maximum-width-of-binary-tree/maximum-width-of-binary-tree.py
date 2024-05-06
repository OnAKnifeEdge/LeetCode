# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_width = 1
        q = deque([(root, 0)])

        while q:
            n = len(q)
            _, start_idx = q[0]
            for _ in range(n):
                current, idx = q.popleft()
                if current.left:
                    q.append((current.left, 2 * idx))
                if current.right:
                    q.append((current.right, 2 * idx + 1))
            max_width = max(max_width, idx - start_idx + 1)
        return max_width
