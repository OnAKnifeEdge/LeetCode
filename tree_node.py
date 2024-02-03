class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def binaryTree(self, arr):
        if not arr:
            return None
        N = len(arr)
        root = TreeNode(arr[0])
        queue = [root]
        i = 1
        while queue:
            cur = queue.pop(0)
            if i < N:
                if arr[i] is not None:
                    cur.left = TreeNode(arr[i])
                    queue.append(cur.left)
                i += 1
                if i < N:
                    if arr[i] is not None:
                        cur.right = TreeNode(arr[i])
                        queue.append(cur.right)
                    i += 1
        return root
