class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)
        cnt = 0
        for i, c in enumerate(s):
            if c.isdigit():
                cnt = max(cnt - 1, 0)
            else:
                s[cnt] = c
                cnt += 1
        s = s[:cnt]
        return "".join(s)
