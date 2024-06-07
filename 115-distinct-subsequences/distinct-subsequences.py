class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # top down approach
        # @cache
        # def dp(i, j):
        #     if j == len(t):  # match empty string t
        #         return 1
        #     if i == len(s):  # s[i:] is empty
        #         return 0
        #     if s[i] == t[j]:
        #         # aab, ab => a_b, _ab
        #         # Two choices: select s[i] or skip s[i]
        #         return dp(i + 1, j + 1) + dp(i + 1, j)
        #         # 选 s 里的，(i + 1, j + 1)
        #         # 不选 s 里的， (i + 1, j)

        #     else:
        #         # Can only skip s[i]
        #         return dp(i + 1, j)

        # return dp(0, 0)

        # bottom up approach
        # ROWS = len(s)
        # COLS = len(t)
        # dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        # for i in range(ROWS + 1):
        #     dp[i][-1] = 1

        # for i in reversed(range(ROWS)):
        #     for j in reversed(range(COLS)):
        #         if s[i] == t[j]:
        #             dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
        #         else:
        #             dp[i][j] = dp[i + 1][j]
        # return dp[0][0]

        # bottom up with space optimization
        ROWS = len(s)
        COLS = len(t)
        dp = [0] * (COLS + 1)
        dp[-1] = 1

        for i in reversed(range(ROWS)):
            prev_dp = dp[:]
            for j in reversed(range(COLS)):
                if s[i] == t[j]:
                    dp[j] = prev_dp[j + 1] + prev_dp[j]
                else:
                    dp[j] = prev_dp[j]
        return dp[0]
