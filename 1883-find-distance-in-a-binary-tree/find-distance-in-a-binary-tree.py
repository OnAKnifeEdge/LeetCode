# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:

        def find_lca(root, p, q):
            if root is None or root.val == p or root.val == q:
                return root
            left = find_lca(root.left, p, q)
            right = find_lca(root.right, p, q)
            if left and right:
                return root
            return left if left else right

        lca = find_lca(root, p, q)

        def bfs(root, p, q):
            queue = deque([(root, 0)])  # (node, depth)
            distances = {p: -1, q: -1}  # To store distances to p and q
            while queue:
                node, depth = queue.popleft()

                # If we've already found both distances, we can return the result
                if distances[p] != -1 and distances[q] != -1:
                    return distances[p] + distances[q]

                # Update the distance if we find p or q
                if node.val == p:
                    distances[p] = depth
                elif node.val == q:
                    distances[q] = depth

                # Continue with the BFS
                if node.left:
                    queue.append((node.left, depth + 1))
                if node.right:
                    queue.append((node.right, depth + 1))

            # In case we exit without finding both nodes, return their combined distance
            return distances[p] + distances[q]

        return bfs(lca, p, q)
