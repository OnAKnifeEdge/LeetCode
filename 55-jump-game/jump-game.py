class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        n = len(nums)
        for i in range(n - 1):
            farthest = max(i + nums[i], farthest)
            if farthest <= i:
                return False
        return farthest >= n - 1

    def canJump_2(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in reversed(range(len(nums))):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
