from typing import List


class Solution:
    # https://leetcode.com/problems/jump-game/
    def can_jump(self, nums):
        if not nums:
            return True
        reach = 0
        for i in range(len(nums)):
            if i > reach:
                break
            reach = max(reach, i + nums[i])
        return reach >= len(nums) - 1

    def canJump(self, nums: List[int]) -> bool:
        r = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= r:
                r = i
        return r == 0
