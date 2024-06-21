class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        first_buy, first_sell = float('-inf'), 0
        second_buy, second_sell = float('-inf'), 0

        for price in prices:
            first_buy = max(first_buy, -price)
            first_sell = max(first_sell, first_buy + price)
            second_buy = max(second_buy, first_sell - price)
            second_sell = max(second_sell, second_buy + price)
        return max(first_sell, second_sell)
        