class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = [-1]
        longest = 0
        for i, c in enumerate(s):
            if c == '(':
                stk.append(i)
            else:
                stk.pop()
                if not stk:
                    stk.append(i)
                else:
                    longest = max(longest, i - stk[-1])
        return longest