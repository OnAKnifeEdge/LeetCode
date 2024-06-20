class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy_cost, sell = prices[0], 0
        for price in prices:
            buy_cost = min(buy_cost, price)
            sell = max(sell, price - buy_cost)
        return sell
