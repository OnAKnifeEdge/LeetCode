class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        N = len(nums)
        result = 0
        for num in nums:
            result |= num
        return result << (N - 1)
