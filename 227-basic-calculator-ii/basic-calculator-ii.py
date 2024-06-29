class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        sign = "+"
        stack = []
        s = s.replace(" ", "")
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            if not c.isdigit() or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / num))
                sign = c
                num = 0
        return sum(stack)
