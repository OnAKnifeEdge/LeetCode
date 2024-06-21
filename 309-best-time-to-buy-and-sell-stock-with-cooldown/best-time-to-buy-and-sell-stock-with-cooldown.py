class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, cooldown, sold = float("-inf"), 0, 0

        for price in prices:
            prev_sold = sold
            # Realize profit from selling the stock bought
            sold = max(sold, buy + price)
            # Keeping the current bought stock or buying new after cooldown
            buy = max(buy, cooldown - price)
            # Transition into cooldown after selling or stay in cooldown
            cooldown = max(cooldown, prev_sold)
        return max(sold, cooldown)
