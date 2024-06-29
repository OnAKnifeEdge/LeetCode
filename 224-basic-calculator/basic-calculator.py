class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        sign = "+"  # the sign before num
        sign_dict = {"+": 1, "-": -1}
        result = 0
        stack = []

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-":
                result += num * sign_dict[sign]
                sign = c
                num = 0 # reset num
            elif c == "(":
                stack.append(result)
                stack.append(sign)
                result = 0 # reset result
                sign = "+" 
            elif c == ")":
                result += num * sign_dict[sign]
                result *= sign_dict[stack.pop()]
                result += stack.pop()
                num = 0 # reset num
        return result + num * sign_dict[sign]
