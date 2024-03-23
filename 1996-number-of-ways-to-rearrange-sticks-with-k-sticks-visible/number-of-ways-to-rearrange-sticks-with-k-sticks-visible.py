class Solution:
    MOD = 10**9 + 7

    def rearrangeSticks(self, n: int, k: int) -> int:
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        # base case
        # if n < k -> 0
        # if n == k -> 1

        for i in range(n):
            for j in range(k):
                if i == j:
                    dp[i][j] = 1

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = dp[i - 1][j - 1] + (i - 1) * dp[i - 1][j]

        return dp[n][k] % Solution.MOD