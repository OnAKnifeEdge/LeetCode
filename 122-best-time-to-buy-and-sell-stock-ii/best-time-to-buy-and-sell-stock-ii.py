class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        # buy: Maximum profit till now with the last action being a buy
        # sell: Maximum profit till now with the last action being a sell
        # buy is initially -infinity because we have not made any purchase yet,
        # thus cannot have a 'profit' from buying
        # sell is 0 because no transaction is a valid initial state with 0 profit

        buy, sell = float('-inf'), 0
        for price in prices:
            # Can we make more money by buying today
            buy = max(buy, sell - price)
            # Can we make more money by selling today
            sell = max(sell, buy + price)
        return sell
