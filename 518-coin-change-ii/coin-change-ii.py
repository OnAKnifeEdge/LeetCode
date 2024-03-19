class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # If we choose to take a coin with value, 
        # we are now searching for a combination of coins that sum up to amount - value. 
        # If we choose to skip the coin, 
        # we are still looking for a combination of coins that sum up to amount, but with fewer coins.

        # base case: 1. if amount == 0, n = 1; 2. if i == len(coins), n = 0

        # # TOP DOWN Apprpoach

        # memo = {}
        # def dp(i, amount):
        #     if amount == 0:
        #         return 1
        #     if i == len(coins):
        #         return 0
        #     if (i, amount) in memo:
        #         return memo[(i, amount)]
        #     if coins[i] > amount:
        #         memo[(i, amount)] = dp(i + 1, amount)
        #     else:
        #         memo[(i, amount)] = dp(i, amount - coins[i]) + dp(i + 1, amount)
        #     return memo[(i, amount)]

        # return dp(0, amount)

        # # BOTTOM UP Approach
        n = len(coins)

        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n):
            dp[i][0] = 1

        for i in reversed(range(n)):
            for a in range(1, amount + 1):
                if coins[i] > a:
                    dp[i][a] = dp[i + 1][a]
                else:
                    dp[i][a] = dp[i][a - coins[i]] + dp[i + 1][a]

        return dp[0][amount]
