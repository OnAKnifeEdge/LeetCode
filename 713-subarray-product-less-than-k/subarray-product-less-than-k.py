class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        # https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/
        if k <= 1:  # If k is 0 or 1, no product can be strictly less than k.
            return 0

        window = 1
        result = 0
        left = 0

        for right in range(len(nums)):
            window *= nums[right]

            while left <= right and window >= k:
                window /= nums[left]
                left += 1

            if window < k:
                result += right - left + 1

        return result
