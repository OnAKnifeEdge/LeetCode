# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        r = []  # array of the largest value in each row of the tree
        if not root:
            return r
        q = deque([root])
        while q:
            n = len(q)
            largest = q[0].val
            for _ in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                largest = max(largest, node.val)
            r.append(largest)
        return r
