class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        parent = None
        stack = []  # decreasing stack simulates the left edges of the BST

        for num in preorder:
            while stack and num > stack[-1]:
                parent = stack.pop()
            # reach to a node which should be in the right tree
            if parent and num <= parent:
                return False
            # If the current number passed the parent check or the parent is still None,
            # we append the current number to the stack, possibly becoming a new parent.
            stack.append(num)
        return True
