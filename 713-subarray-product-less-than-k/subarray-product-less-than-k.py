class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        # https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/
        if k <= 1: # If k is 0 or 1, no product can be strictly less than k.
            return 0

        prefix_product = 1
        result = 0
        left = 0

        for right in range(len(nums)):
            prefix_product *= nums[right]

            while left <= right and prefix_product >= k:
                prefix_product /= nums[left]
                left += 1

            if prefix_product < k:
                l = right - left + 1
                result += l

        return result