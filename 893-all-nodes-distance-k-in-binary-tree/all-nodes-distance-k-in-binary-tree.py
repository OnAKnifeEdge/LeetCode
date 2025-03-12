# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def distanceK(self, root: TreeNode, target: int, k: int) -> List[int]:
        """Find all nodes at distance k from target node."""
        visited = set()  # Store TreeNode objects
        answer = []

        def build_path(node: TreeNode, path: List[TreeNode]) -> bool:
            if not node:
                return False
            path.append(node)
            if node.val == target.val:  # Compare value to target (int)
                return True
            if build_path(node.left, path):
                return True
            if build_path(node.right, path):
                return True
            path.pop()
            return False

        def dfs(node, depth) -> None:
            """Collect nodes at given depth downward, tracking visited nodes."""
            if not node or node in visited:
                return
            visited.add(node)  # Add node to visited
            if depth == 0:
                answer.append(node.val)
                return
            dfs(node.left, depth - 1)
            dfs(node.right, depth - 1)

        # Step 1: Build path to target
        path = []
        if not build_path(root, path):
            return []

        # Step 2: Collect nodes k distance below target
        target_node = path[-1]  # Target is now included in path
        dfs(target_node, k)

        # Step 3: Walk up the path, adjusting distance
        dist = k - 1
        for i in reversed(range(1, len(path))):  # From target up to root (exclusive)
            curr = path[i - 1]  # Parent node
            child = path[i]  # Child we came from
            if dist == 0:  # If distance hits 0, add the ancestor node
                if curr not in visited:
                    answer.append(curr.val)
                break
            # Collect from the opposite child
            opposite = curr.right if curr.left == child else curr.left
            dfs(opposite, dist - 1)
            dist -= 1

        return answer
