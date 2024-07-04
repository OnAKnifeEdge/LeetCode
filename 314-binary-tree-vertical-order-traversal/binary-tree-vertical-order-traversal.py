# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = deque([(root, 0)])
        d = defaultdict(list)

        while q:
            node, col = q.popleft()
            d[col].append(node.val)
            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))

        return [d[x] for x in sorted(d.keys())]

        # left, right = min(d.keys()), max(d.keys())

        # result = []
        # for i in range(left, right + 1):
        #     result.append(d[i])

        # return result
