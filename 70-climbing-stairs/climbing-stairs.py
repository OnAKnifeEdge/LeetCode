class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] = dp[i - 1] + dp[i - 2]
        a, b = 1, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
