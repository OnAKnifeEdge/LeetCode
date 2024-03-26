class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i -2])
        two_back, one_back = 0, 0
        for i in range(2, len(cost) + 1):
            one_back, two_back = min(two_back + cost[i - 2], one_back + cost[i - 1]), one_back
        return one_back
