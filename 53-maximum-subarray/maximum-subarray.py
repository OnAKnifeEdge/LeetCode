class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = 0
        min_prefix_sum = 0
        max_sum = float("-inf")

        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum)

        return max_sum
