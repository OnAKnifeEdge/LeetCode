class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithms
        max_sum = nums[0]
        max_ending_so_far = nums[0]

        for num in nums[1:]:
            max_ending_so_far = max(num, max_ending_so_far + num)
            max_sum = max(max_sum, max_ending_so_far)

        return max_sum

        # prefix_sum solution
        # prefix_sum = 0
        # min_prefix_sum = 0
        # max_sum = float("-inf")

        # for num in nums:
        #     prefix_sum += num
        #     max_sum = max(max_sum, prefix_sum - min_prefix_sum)
        #     min_prefix_sum = min(min_prefix_sum, prefix_sum)

        # return max_sum
