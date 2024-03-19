class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}

        for i in reversed(range(len(days))):
            dp[i] = float('inf')
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dp.get(j, 0))
        return dp[0]




        # cache = {}

        # def dp(i):
        #     if i == len(days):
        #         return 0
        #     if i in cache:
        #         return cache[i]
            
        #     cache[i] = float("inf")
        #     for d, c in zip([1, 7, 30], costs):
        #         j = i
        #         while j < len(days) and days[j] < days[i] + d:
        #             j += 1
        #         cache[i] = min(cache[i], c + dp(j))
        #     return cache[i]

        # return dp(0)
