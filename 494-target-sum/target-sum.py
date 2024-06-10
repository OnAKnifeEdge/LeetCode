class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # memo = {}  # (i, target) => number of ways

        @cache
        def dp(i, total):
            if i == len(nums):  # reached the end
                return 1 if total == target else 0
            return dp(i + 1, total + nums[i]) + dp(i + 1, total - nums[i])
            # return memo[(i, total)]

        return dp(0, 0)
