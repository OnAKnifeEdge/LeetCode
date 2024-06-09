class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)

        # dp[i][sum]
        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            for s in range(subset_sum + 1):
                num = nums[i - 1]
                if s < num:
                    dp[i][s] = dp[i - 1][s]  # do not include i
                else:
                    dp[i][s] = dp[i - 1][s] or dp[i - 1][s - num]
                if s == subset_sum and dp[i][s]:
                    return True

        return False
