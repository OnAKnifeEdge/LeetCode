class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        end, far = 0, 0

        for i in range(n - 1):
            far = max(far, i + nums[i])

            if i == end:
                count += 1
                end = far
        return count
        