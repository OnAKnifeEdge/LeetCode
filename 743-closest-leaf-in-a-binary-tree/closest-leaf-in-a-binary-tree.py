# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

    def __init__(self):
        self.val_to_parent = {}

    def traverse(self, node: Optional[TreeNode], parent: Optional[TreeNode]) -> int:
        if not node:
            return
        self.val_to_parent[node.val] = (node, parent)
        self.traverse(node.left, node)
        self.traverse(node.right, node)

    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        self.traverse(root, None)
        target_node, _ = self.val_to_parent[k]
        q = deque([target_node])
        visited = {target_node.val}
        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                _, parent_node = self.val_to_parent[node.val]
                if parent_node and parent_node.val not in visited:
                    q.append(parent_node)
                    visited.add(parent_node.val)
                if node.left and node.left.val not in visited:
                    q.append(node.left)
                    visited.add(node.left.val)
                if node.right and node.right.val not in visited:
                    q.append(node.right)
                    visited.add(node.right.val)
                if not node.left and not node.right:
                    return node.val
        return -1
