class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        q = deque(s)

        def process(q):
            num = 0
            sign = "+"
            stack = []

            while q:
                c = q.popleft()
                if c.isdigit():
                    num = num * 10 + int(c)
                elif c == "(":
                    # start recursion
                    num = process(q)
                if c in "+-*/)" or not q:
                    if sign == "+":
                        stack.append(num)
                    elif sign == "-":
                        stack.append(-num)
                    elif sign == "*":
                        stack.append(stack.pop() * num)
                    elif sign == "/":
                        stack.append(int(stack.pop() / num))
                    num = 0
                    sign = c
                    if c == ")":
                        break
            return sum(stack)

        return process(q)
