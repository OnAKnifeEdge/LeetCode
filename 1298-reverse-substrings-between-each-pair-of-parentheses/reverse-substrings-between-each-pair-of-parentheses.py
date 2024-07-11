class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = []
        pair = [0] * n

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                j = stack.pop()
                pair[i] = j
                pair[j] = i

        result = []
        curr = 0
        direction = 1

        while curr < n:
            if s[curr] == "(" or s[curr] == ")":
                curr = pair[curr]
                direction = -direction
            else:
                result.append(s[curr])
            curr += direction

        return "".join(result)
