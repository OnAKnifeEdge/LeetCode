class Solution:
    def minDifference(self, nums: List[int]) -> int:
        k = 4
        nums.sort()
        n = len(nums)
        if n <= k:
            return 0

        min_diff = float("inf")
        # remove smallest: 0, 1, 2, 3
        for i in range(k):
            j = n - k + i
            min_diff = min(min_diff, nums[j] - nums[i])
        return min_diff
        # return min(
        #     nums[-1] - nums[3],  # Remove 3 smallest
        #     nums[-2] - nums[2],  # Remove 2 smallest and 1 largest
        #     nums[-3] - nums[1],  # Remove 1 smallest and 2 largest
        #     nums[-4] - nums[0],  # Remove 3 largest
        # )
