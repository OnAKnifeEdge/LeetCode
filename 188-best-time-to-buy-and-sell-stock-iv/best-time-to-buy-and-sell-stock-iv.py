class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        if k >= n // 2:
            # 122. Best Time to Buy and Sell Stock II
            # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
            buy, sell = float("-inf"), 0
            for price in prices:
                buy = max(buy, sell - price)
                sell = max(sell, buy + price)
            return sell

        buy = [float("-inf")] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):
                buy[i] = max(buy[i], sell[i - 1] - price)
                sell[i] = max(sell[i], buy[i] + price)
        return sell[k]
