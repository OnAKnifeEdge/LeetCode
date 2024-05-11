class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # 先让 num 里的数字单调递增
        # 如果可以继续删，删最后一位
        mono_stack = []
        for digit in num:
            while mono_stack and mono_stack[-1] > digit and k > 0:
                # if current digit is smaller, we pop the stack
                mono_stack.pop()
                k -= 1
            mono_stack.append(digit)

        result = mono_stack[:-k] if k > 0 else mono_stack
        return "".join(result).lstrip("0") or "0"
