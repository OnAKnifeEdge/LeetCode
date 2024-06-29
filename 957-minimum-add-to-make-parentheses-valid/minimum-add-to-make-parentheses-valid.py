class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for c in s:
            # 如果是左括号，就入栈。当右括号时，同时栈顶为左括号时，则将左括号排出，最后留在栈内的括号数量就是需要加入的括号数量
            if c == "(":
                stack.append(c)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(c)
        return len(stack)
