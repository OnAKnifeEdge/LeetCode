class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        end, farthest = 0, 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                count += 1
                end = farthest
        return count
