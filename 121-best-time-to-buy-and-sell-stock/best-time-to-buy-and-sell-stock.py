class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy, sell = float('-inf'), 0

        for price in prices:
            buy = max(buy, -price)
            sell = max(sell, buy + price)

        return sell
        