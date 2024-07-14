class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for i in range(len(nums)):
            a, b = b, max(b, a + nums[i])
        return b
