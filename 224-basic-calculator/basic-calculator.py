from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")

        def process(q):
            stack = []
            sign = "+"
            num = 0

            while q:
                c = q.popleft()
                if c.isdigit():
                    num = 10 * num + int(c)
                elif c == "(":
                    num = process(q)
                if c in "+-*/" or c == ")" or not q:
                    if sign == "+":
                        stack.append(num)
                    elif sign == "-":
                        stack.append(-num)
                    elif sign == "*":
                        stack.append(stack.pop() * num)
                    elif sign == "/":
                        stack.append(int(stack.pop() // num))  # Use integer division
                    num = 0
                    sign = c
                    if c == ")":
                        break
            
            return sum(stack)
        
        return process(deque(s))

