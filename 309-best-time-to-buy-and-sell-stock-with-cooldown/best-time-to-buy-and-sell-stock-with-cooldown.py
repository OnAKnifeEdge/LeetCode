class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cooldown, sold, hold = 0, 0, float('-inf') # 股票不可能無中生有，免費獲得利潤，所以 hold 要記得初始化成負無窮大。

        for price in prices:
            prev_sold = sold

            # cooldown on day i: cooldown of day (i - 1), or sell out of day (i - 1). day i is a cooling day 
            sold = hold + price
            hold = max(hold, cooldown - price)
            cooldown = max(cooldown, prev_sold)

        return max(sold, cooldown)
        