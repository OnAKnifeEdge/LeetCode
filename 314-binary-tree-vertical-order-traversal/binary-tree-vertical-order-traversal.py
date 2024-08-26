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
        d = defaultdict(list)
        q = deque([(root, 0)])
        min_c, max_c = 0, 0
        while q:
            node, col = q.popleft()
            if node is not None:
                min_c = min(min_c, col)
                max_c = max(max_c, col)
                d[col].append(node.val)
                q.append([node.left, col - 1])
                q.append([node.right, col + 1])

        return [d[col] for col in range(min_c, max_c + 1)]
