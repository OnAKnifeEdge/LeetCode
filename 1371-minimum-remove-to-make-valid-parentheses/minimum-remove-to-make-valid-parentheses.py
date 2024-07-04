class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        altered = list(s)

        for i, c in enumerate(altered):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    altered[i] = ""

        while stack:
            altered[stack.pop()] = ""

        return "".join(altered)
