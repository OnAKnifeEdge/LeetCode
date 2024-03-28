class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cooldown, sell, hold = 0, 0, float('-inf') # 股票不可能無中生有，免費獲得利潤，所以 hold 要記得初始化成負無窮大。

        for price in prices:
            prev_cooldown, prev_sell, prev_hold = cooldown, sell, hold

            cooldown = max(prev_cooldown, prev_sell)
            sell = prev_hold + price
            hold = max(prev_hold, prev_cooldown - price)

        return max(sell, cooldown)
        