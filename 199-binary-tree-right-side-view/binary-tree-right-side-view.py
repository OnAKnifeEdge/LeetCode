# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        next_level = deque([root])
        rightside = []

        while next_level:
            current_level = next_level
            next_level = deque()

            while current_level:
                node = current_level.popleft()

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            rightside.append(node.val)
        return rightside



        # # levels
        # if not root:
        #     return []
        # q = deque([root])
        # rightside = []
        # while q:
        #     levels = len(q)
        #     for i in range(levels):
        #         node = q.popleft()
        #         if i == levels - 1:
        #             rightside.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # return rightside
        