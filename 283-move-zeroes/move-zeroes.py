class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        non_zero_idx = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[non_zero_idx] = num
                non_zero_idx += 1
        nums[non_zero_idx:n] = [0] * (n - non_zero_idx)
