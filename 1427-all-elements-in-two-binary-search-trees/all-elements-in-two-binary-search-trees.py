# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


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

    def getAllElementsIDontKnow(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2, output = [], [], []

        while root1 or root2 or stack1 or stack2:
            # update both stacks
            # by going left till possible
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left

            # Add the smallest value into output,
            # pop it from the stack,
            # and then do one step right
            if not stack2 or stack1 and stack1[-1].val <= stack2[-1].val:
                root1 = stack1.pop()
                output.append(root1.val)
                root1 = root1.right
            else:
                root2 = stack2.pop()
                output.append(root2.val)
                root2 = root2.right

        return output
