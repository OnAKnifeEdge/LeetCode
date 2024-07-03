class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 4:
            return 0
        return min(
            nums[-1] - nums[3],  # Remove 3 smallest
            nums[-2] - nums[2],  # Remove 2 smallest and 1 largest
            nums[-3] - nums[1],  # Remove 1 smallest and 2 largest
            nums[-4] - nums[0],  # Remove 3 largest
        )
