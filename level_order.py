# Definition for a binary tree node.
from collections import deque
from typing import Optional, List

import tree_node
from tree_node import TreeNode


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    levels = []
    if not root:
        return levels
    q = deque([(root, 0)])
    while q:
        node, level = q.popleft()
        if len(levels) == level:
            levels.append([])
        levels[level].append(node.val)
        if node.left:
            q.append((node.left, level + 1))
        if node.right:
            q.append((node.right, level + 1))
    return levels


arr = [3, 9, 20, None, None, 15, 7]
node = tree_node.TreeNode().binaryTree(arr)
print(levelOrder(node))
