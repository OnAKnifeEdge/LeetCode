class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = nums[0]
        max_global = max_current = nums[0]
        min_global = min_current = nums[0]

        for num in nums[1:]:
            max_current = max(num, num + max_current)
            max_global = max(max_current, max_global)

            min_current = min(num, num + min_current)
            min_global = min(min_current, min_global)

            total += num

        if max_global < 0:
            return max_global

        return max(max_global, total - min_global)
