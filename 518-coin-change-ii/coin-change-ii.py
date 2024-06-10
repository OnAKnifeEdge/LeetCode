class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 若只使用前 i 个物品（可以重复使用），当背包容量为 j 时，有 dp[i][j] 种方法可以装满背包。
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1  # if amount is 0, there is only 1 way

        """
        The loop over the coins should be the outer loop,
        and the loop over the amounts should be the inner loop.
        This is to ensure the i - 1 states do not get overwritten
        before they have been used to calculate the i states,
        as i represents the number of kinds of coins used.
        """
        for i in range(n):
            for amt in range(1, amount + 1):
                dp[i][amt] = dp[i - 1][amt] if i >= 1 else 0
                if amt >= coins[i]:
                    dp[i][amt] += dp[i][amt - coins[i]]
        return dp[n - 1][amount]
