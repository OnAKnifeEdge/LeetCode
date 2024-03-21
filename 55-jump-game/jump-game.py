class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r = len(nums) - 1
        for i in reversed(range(len(nums))):
            if i + nums[i] >= r:
                r = i
        return r == 0