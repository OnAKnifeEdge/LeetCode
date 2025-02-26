class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix_sum = 0
        min_prefix = 0
        max_prefix = 0
        for num in nums:
            prefix_sum += num
            min_prefix = min(prefix_sum, min_prefix)
            max_prefix = max(prefix_sum, max_prefix)

        return max_prefix - min_prefix
