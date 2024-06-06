class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @cache
        def dp(i, j):
            if j == len(t):  # match empty string t
                return 1
            if i == len(s):  # s[i:] is empty
                return 0
            if s[i] == t[j]:
                # aab, ab => a_b, _ab
                # Two choices: select s[i] or skip s[i]
                return dp(i + 1, j + 1) + dp(i + 1, j)
                # 选 s 里的，(i + 1, j + 1)
                # 不选 s 里的， (i + 1, j)

            else:
                # Can only skip s[i]
                return dp(i + 1, j)

        return dp(0, 0)
