from enum import Enum


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Camera(Enum):
    NEEDS_CAMERA = 0
    COVERED = 1
    HAS_CAMERA = 2


class Solution:

    def __init__(self):
        self.camera = 0

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if self.cover(root) == Camera.NEEDS_CAMERA:
            self.camera += 1
        return self.camera

    def cover(self, node) -> int:
        if not node:
            return Camera.COVERED
        left = self.cover(node.left)
        right = self.cover(node.right)
        if left == Camera.NEEDS_CAMERA or right == Camera.NEEDS_CAMERA:
            self.camera += 1
            return Camera.HAS_CAMERA

        if left == Camera.HAS_CAMERA or right == Camera.HAS_CAMERA:
            return Camera.COVERED

        return Camera.NEEDS_CAMERA
