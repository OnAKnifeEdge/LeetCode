# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_to_left(root)

    def _push_to_left(self, node: Optional[TreeNode]):
        while node:
            self.stack.append(node)
            node = node.left

    def peek(self):
        return self.stack[-1].val

    def next(self):
        smallest = self.stack.pop()
        self._push_to_left(smallest.right)
        return smallest.val

    def hasNext(self):
        return bool(self.stack)


class Solution:
    # 173, 21
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        i1 = BSTIterator(root1)
        i2 = BSTIterator(root2)

        result = []

        while i1.hasNext() and i2.hasNext():
            if i1.peek() < i2.peek():
                result.append(i1.next())
            else:
                result.append(i2.next())

        while i1.hasNext():
            result.append(i1.next())

        while i2.hasNext():
            result.append(i2.next())

        return result
