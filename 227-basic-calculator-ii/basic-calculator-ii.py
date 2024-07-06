class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        n = len(s)

        stack = []
        num = 0
        previous_sign = "+"

        for i in range(n):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            if not c.isdigit() or i == n - 1:
                if previous_sign == "+":
                    stack.append(num)
                elif previous_sign == "-":
                    stack.append(-num)
                elif previous_sign == "*":
                    stack.append(stack.pop() * num)
                elif previous_sign == "/":
                    stack.append(int(stack.pop() / num))
                previous_sign = c
                num = 0

        return sum(stack)
