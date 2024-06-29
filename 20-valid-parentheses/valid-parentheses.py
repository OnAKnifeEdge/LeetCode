class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if c in parentheses.values():
                stack.append(c)
            elif c in parentheses.keys():
                if not stack:
                    return False
                if stack.pop() != parentheses[c]:
                    return False
            else:
                return False
        return not bool(stack)
