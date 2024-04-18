# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



    # def inorder(r):
    #     if not r or len(ans) >= k:
    #         return
    #     inorder(r.left)
    #     if len(ans) < k:
    #         ans.append(r.val)
    #         inorder(r.right)

    # ans = []
    # inorder(root)
    # return ans[-1]



class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(r):
            if not r or len(result) >= k:
                return
            inorder(r.left)
            if len(result) >= k:
                return
            result.append(r.val)
            inorder(r.right)

        result = []
        inorder(root)
        return result[-1]
        