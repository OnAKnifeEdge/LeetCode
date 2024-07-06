class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        n = len(s)

        stack = []
        num = 0
        sign = "+"

        for i in range(n):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            if not c.isdigit() or i == n - 1:
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
