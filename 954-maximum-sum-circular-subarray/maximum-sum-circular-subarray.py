class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]

        max_so_far = nums[0]
        min_so_far = nums[0]

        total = nums[0]

        for num in nums[1:]:
            total += num
            min_so_far = min(num, num + min_so_far)
            min_sum = min(min_sum, min_so_far)
            max_so_far = max(num, num + max_so_far)
            max_sum = max(max_sum, max_so_far)

        if max_sum < 0:
            return max_sum

        circular_max_sum = total - min_sum
        return max(circular_max_sum, max_sum)

            
        