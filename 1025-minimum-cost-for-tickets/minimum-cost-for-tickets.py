class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = {}

        def dp(i):
            if i == len(days):
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = float("inf")
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                cache[i] = min(cache[i], c + dp(j))
            return cache[i]

        return dp(0)
