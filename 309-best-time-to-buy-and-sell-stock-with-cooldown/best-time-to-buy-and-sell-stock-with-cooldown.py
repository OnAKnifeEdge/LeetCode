class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state: buying or selling
        # if buy => i + 1
        # if sell => i + 2 we have to take a cooldown day

        dp = {} # key = {i, buying} val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)] 

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, False) - prices[i]       
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        return dfs(0, True)

