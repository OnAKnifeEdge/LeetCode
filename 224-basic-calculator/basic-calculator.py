class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")

        def process(q) -> int:
            stack = []
            sign = "+"
            num = 0

            while q:
                c = q.popleft()
                if c.isdigit():
                    num = 10 * num + int(c)
                # 遇到左括号开始递归计算 num
                elif c == "(":
                    num = process(q)
                if c in "+-*/)" or not q:
                    if sign == "+":
                        stack.append(num)
                    elif sign == "-":
                        stack.append(-num)
                    elif sign == "*":
                        stack.append(stack.pop() * num)
                    elif sign == "/":
                        stack.append(stack.pop() // num)
                    num = 0
                    sign = c
                    # 遇到右括号返回递归结果
                    if c == ")":
                        break
            return sum(stack)

        return process(deque(s))
