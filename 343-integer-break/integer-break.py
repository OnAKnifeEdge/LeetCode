class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1

        for num in range(2, n + 1):
            if num == n:
                dp[num] = 0
            else:
                dp[num] = num
            for i in range(1, num):
                dp[num] = max(dp[num], dp[i] * dp[num - i])

        return dp[n]

        # def dfs(num):
        #     if num in dp:
        #         return dp[num]
        #     dp[num] = 0 if num == n else num
        #     for i in range(1, num):
        #         val = dfs(i) * dfs(num - i)
        #         dp[num] = max(dp[num], val)
        #     return dp[num]

        # return dfs(n)
