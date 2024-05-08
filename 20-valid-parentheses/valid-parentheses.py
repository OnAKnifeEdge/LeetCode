class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c in mapping.values():
                stack.append(c)
            elif c in mapping.keys():
                if not stack or mapping[c] != stack.pop():
                    return False
            else:
                return False
        return len(stack) == 0

