class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        parent = None
        stack = []  # decresing

        for num in preorder:
            while stack and num > stack[-1]:
                parent = stack.pop()
            if parent and num <= parent:
                return False
            stack.append(num)
        return True
