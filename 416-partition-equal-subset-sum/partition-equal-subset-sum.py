class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2

        dp = [False] * (subset_sum + 1)
        # dp[i]: it's possible to get a subset sum of i using numbers seen so far.
        dp[0] = True  # 背包没有空间的时候，就相当于装满了
        for num in nums:
            for i in reversed(range(subset_sum + 1)):
                if num <= i:
                    dp[i] = dp[i] or dp[i - num]
        return dp[subset_sum]

    # 给一个可装载重量为 sum / 2 的背包和 N 个物品，每个物品的重量为 nums[i]。现在让你装物品，是否存在一种装法，能够恰好将背包装满？
    def canPartition_dp(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)

        # dp[i][sum]
        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(subset_sum + 1):
                num = nums[i - 1]
                if num > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]
        return dp[n][subset_sum]
