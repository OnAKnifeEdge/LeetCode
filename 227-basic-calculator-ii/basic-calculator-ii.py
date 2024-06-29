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
            if c in "+-*/" or i == len(s) - 1:  # Process num when an operator or end is reached
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)  # Evaluate * immediately
                elif sign == "/":
                    stack.append(int(stack.pop() / num)) # Evaluate / immediately
                sign = c  
                num = 0  
        return sum(stack)