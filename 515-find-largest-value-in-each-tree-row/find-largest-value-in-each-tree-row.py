# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        r = []
        if not root:
            return r

        def dfs(node: Optional[root], depth):
            if not node:
                return

            if depth == len(r):
                r.append(node.val)
            else:
                r[depth] = max(r[depth], node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return r



    def largestValuesBFS(self, root: Optional[TreeNode]) -> List[int]:
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
