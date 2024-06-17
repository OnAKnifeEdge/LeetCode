class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        # dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + points[i]*points[j]*points[k])
        # 从下往上，从左往右
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                for k in range(i + 1, j):
                    dp[i][j] = max(
                        dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[j] * nums[k]
                    )

        return dp[0][n - 1]
