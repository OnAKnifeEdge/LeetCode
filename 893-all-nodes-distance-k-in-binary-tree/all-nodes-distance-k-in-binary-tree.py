# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.parent = {}  # {node.val: parent_node}

    def traverse(self, node: TreeNode, parent: TreeNode):
        if not node:
            return
        self.parent[node.val] = parent
        self.traverse(node.left, node)
        self.traverse(node.right, node)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        self.traverse(root, None)
        q = deque([target])
        visited = {target.val}
        distance = 0
        l = []

        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if distance == k:
                    l.append(node.val)
                parent_node = self.parent[node.val]
                if parent_node and parent_node.val not in visited:
                    q.append(parent_node)
                    visited.add(parent_node.val)
                if node.left and node.left.val not in visited:
                    q.append(node.left)
                    visited.add(node.left.val)
                if node.right and node.right.val not in visited:
                    q.append(node.right)
                    visited.add(node.right.val)
            distance += 1
        return l
