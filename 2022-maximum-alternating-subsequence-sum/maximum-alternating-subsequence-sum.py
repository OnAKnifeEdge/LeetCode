class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sum_even, sum_odd = 0, 0
        for i in reversed(range(len(nums))):
            tmp_even = max(sum_odd + nums[i], sum_even)
            tmp_odd = max(sum_even - nums[i], sum_odd)
            sum_even, sum_odd = tmp_even, tmp_odd
        return sum_even