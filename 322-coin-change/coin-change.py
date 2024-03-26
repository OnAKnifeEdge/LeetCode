class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], 1 + dp[x - coin])
        
        if dp[amount] != float('inf'):
            return dp[amount]
        return -1
