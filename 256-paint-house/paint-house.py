class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # costs[i][j] i is house, j is color
        # a = b = c = 0

        # for i in range(len(costs)):
        #     a = costs[i][0] + min(b, c)
        #     b = costs[i][1] + min(a, c)
        #     c = costs[i][2] + min(a, b)
        
        # return min(a, b, c)
        dp = [0, 0, 0]
        for i in range(len(costs)):
            a = costs[i][0] + min(dp[1], dp[2])
            b = costs[i][1] + min(dp[0], dp[2])
            c = costs[i][2] + min(dp[0], dp[1])
            dp = [a, b, c]
        return min(dp)