class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c.isdigit() and stack:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
