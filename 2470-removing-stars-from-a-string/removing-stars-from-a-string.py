class Solution:
    def removeStars(self, s: str) -> str:
        if not s:
            return ""
        stack = []
        for c in s:
            if stack and c == "*":
                stack.pop()
                continue
            if c != '*':
                stack.append(c)
        return "".join(stack)
        