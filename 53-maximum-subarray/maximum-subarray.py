class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = nums[0]
        total = nums[0]
        for num in nums[1:]:
            # if total < 0:
            #     total = 0
            # total += num
            total = max(num, total + num)
            largest = max(largest, total)
        return largest
