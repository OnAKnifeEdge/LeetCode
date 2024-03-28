class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)  # row and col

        dp = [[0] * (N + 1) for _ in range(M + 1)]

        for c in range(N + 1):
            # 最后一行 s[] = "", t[]= t[-1]
            dp[M][c] = 0

        for r in range(M + 1):
            # 最后一列 s[] = s[-1], t = ""
            dp[r][N] = 1

        for i in reversed(range(M)):
            for j in reversed(range(N)):
                dp[i][j] = dp[i + 1][j]

                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
        return dp[0][0]  
