class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "]":
                part = ""
                while stack[-1].isalpha():
                    part = stack.pop() + part
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * part)
            else:
                stack.append(c)
        return "".join(stack)
