class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # https://leetcode.com/problems/subarray-product-less-than-k/
        # two-pointer: find the maximum length subarray which has the sum equal to sum(nums) - x. 
        total = sum(nums)
        target = total - x

        n = len(nums)

        if target == 0:
            return n
        
        left = 0
        prefix_sum = 0
        ops = float('inf')

        for right in range(n):
            prefix_sum += nums[right]

            while left < right and prefix_sum > target:
                prefix_sum -= nums[left]
                left += 1

            if prefix_sum == target:
                l = n - (right - left + 1)
                ops = min(ops, l)

        return ops if ops != float('inf') else -1

