# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        largest = []
        while q:
            n = len(q)
            max_level = float("-inf")
            for _ in range(n):
                node = q.popleft()
                max_level = max(max_level, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            largest.append(max_level)
        return largest
