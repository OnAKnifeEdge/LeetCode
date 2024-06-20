class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = float('-inf'), 0
        for price in prices:
            buy = max(buy, sell - price)
            sell = max(sell, buy + price)
        return sell
