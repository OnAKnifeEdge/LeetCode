class Solution:

    def has_match(self, stack, part):
        n = len(part)
        if len(stack) < n:
            return False
        n = len(part)
        return stack[-n:] == list(part)

    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []

        for c in s:
            stack.append(c)
            if self.has_match(stack, part):
                for _ in range(len(part)):
                    stack.pop()

        return "".join(stack)
