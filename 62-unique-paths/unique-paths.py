class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[0] * n for _ in range(m)]

        # for j in range(n):
        #     dp[0][j] = 1
        # for i in range(m):
        #     dp[i][0] = 1

        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # return dp[-1][-1]
        if m < n:
            m, n = n, m
        # n is the smaller open
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
                # cell left: dp[j - 1], prev cell: dp[j]
        return dp[-1]
