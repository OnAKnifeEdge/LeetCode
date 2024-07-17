class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # min(dp[i - 2] + cost[i], dp[i - 1] + cost[i])
        a, b = 0, 0
        for i in range(2, len(cost) + 1):
            a, b = b, min(b + cost[i - 1], a + cost[i - 2])
        return b
