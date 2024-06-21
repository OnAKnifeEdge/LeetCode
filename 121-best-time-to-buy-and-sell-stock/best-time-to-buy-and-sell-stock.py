class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy, sell = float('inf'), 0
        for price in prices:
            buy = min(buy, price)
            sell = max(sell, price - buy)
        return sell
