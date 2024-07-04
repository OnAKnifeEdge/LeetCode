class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return s

        to_remove = set()
        stack = []

        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif not stack:
                to_remove.add(i)
            else:
                stack.pop()

        to_remove = to_remove.union(set(stack))
        result = []
        for i, c in enumerate(s):
            if i not in to_remove:
                result.append(c)

        return ''.join(result)
