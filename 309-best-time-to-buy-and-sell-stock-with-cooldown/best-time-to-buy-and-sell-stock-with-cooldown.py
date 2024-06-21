class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, cooldown, sell = float("-inf"), 0, 0

        for price in prices:
            prev_sold = sell
            # Realize profit from selling the stock bought
            sell = buy + price
            # Keeping the current bought stock or buying new after cooldown
            buy = max(buy, cooldown - price)
            # Transition into cooldown after selling or stay in cooldown
            cooldown = max(cooldown, prev_sold)
        return max(sell, cooldown)
