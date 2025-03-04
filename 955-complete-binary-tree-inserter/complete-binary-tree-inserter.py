# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = deque([])
        self.candidates = deque([])
        if root:
            self.q.append(root)
        while self.q:
            node = self.q.popleft()
            if not node.left or not node.right:
                self.candidates.append(node)
            if node.left:
                self.q.append(node.left)
            if node.right:
                self.q.append(node.right)

    def insert(self, val: int) -> int:
        node = TreeNode(val)
        if not self.candidates:  # If candidates is empty
            if not self.root:    # If tree is empty
                self.root = node
                self.candidates.append(node)
                return val
        parent = self.candidates[0]
        if not parent.left:
            parent.left = node
        else:
            parent.right = node
            self.candidates.popleft()
        self.candidates.append(node)

        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
