class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        #  it's optimal to always remove the substring that gives more points first.
        first, second = ("ab", "ba") if x >= y else ("ba", "ab")
        x, y = max(x, y), min(x, y)
        gain = 0

        def remove(s, target, point):
            stack = []
            nonlocal gain
            for c in s:
                if stack and stack[-1] + c == target:
                    gain += point
                    stack.pop()
                else:
                    stack.append(c)
            return "".join(stack)

        s = remove(s, first, x)
        remove(s, second, y)

        return gain
