class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp = [0] * (len(cost) + 1)

        # for i in range(2, len(cost) + 1):
        #     one = dp[i - 1] + cost[i - 1]
        #     two = dp[i - 2] + cost[i - 2]
        #     dp[i] = min(one, two)
        
        # return dp[-1]

        # @cache
        # def dp(i):
        #     if i <= 1:
        #         return 0
        #     one = dp(i - 1) + cost[i - 1]
        #     two = dp(i - 2) + cost[i - 2]  
        #     return min(one, two)
        # return dp(len(cost))

        one = two = 0
        for i in range(2, len(cost) + 1):
            one, two =  min(one + cost[i - 1], two + cost[i - 2]), one
        return one
