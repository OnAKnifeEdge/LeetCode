class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        sign = 1  # the sign before num
        result = 0
        stack = []

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-":
                result += num * sign
                sign = -1 if c == "-" else 1
                num = 0
            elif c == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif c == ")":
                result += num * sign
                result *= stack.pop()
                result += stack.pop()
                num = 0
        return result + num * sign
