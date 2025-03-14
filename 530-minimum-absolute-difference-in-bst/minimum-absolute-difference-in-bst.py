# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        min_diff = float("inf")
        prev_val = None

        # result = []
        current = root

        while current:

            if not current.left:
                # result.append(current.val)

                if prev_val is not None:
                    min_diff = min(abs(current.val - prev_val), min_diff)
                prev_val = current.val

                current = current.right
            else:
                prev = current.left
                while prev.right and prev.right != current:
                    prev = prev.right

                if not prev.right:
                    prev.right = current
                    current = current.left
                else:
                    prev.right = None

                    # result.append(current.val)
                    if prev_val is not None:
                        min_diff = min(abs(current.val - prev_val), min_diff)
                    prev_val = current.val

                    current = current.right

        return min_diff
