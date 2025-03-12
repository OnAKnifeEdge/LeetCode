# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def build_tree(node, parent):
            if node and parent:
                graph[parent.val].append(node.val)
                graph[node.val].append(parent.val)
            if node.left:
                build_tree(node.left, node)
            if node.right:
                build_tree(node.right, node)

        build_tree(root, None)

        q = deque([(target.val, 0)])
        visited = {target.val}
        answer = []

        while q:
            node, distance = q.popleft()
            if distance == k:
                answer.append(node)
                continue

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, distance + 1))

        return answer
