# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from enum import Enum


class CameraStatus(Enum):
    EMPTY = 0
    COVERED = 1
    HAS_CAMERA = 2


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.camera = 0

        def dfs(node):
            if not node:
                return CameraStatus.COVERED
            left = dfs(node.left)
            right = dfs(node.right)
            if left == CameraStatus.EMPTY or right == CameraStatus.EMPTY:
                self.camera += 1
                return CameraStatus.HAS_CAMERA
            if left == CameraStatus.HAS_CAMERA or right == CameraStatus.HAS_CAMERA:
                return CameraStatus.COVERED
            return CameraStatus.EMPTY
            # this node is not monitored and signals to the parent, “I need coverage.”

        if dfs(root) == CameraStatus.EMPTY:
            self.camera += 1
        return self.camera
