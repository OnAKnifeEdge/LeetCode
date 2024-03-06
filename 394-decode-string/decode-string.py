class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ']':
                current_string = ''
                while stack[-1] != '[':
                    current_string = stack.pop() + current_string
                stack.pop()

                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(current_string * int(num))
            else:
                stack.append(c)
        return ''.join(stack)
                