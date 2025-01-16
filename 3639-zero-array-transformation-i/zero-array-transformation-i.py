class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * n
        for left, right in queries:
            diff[left] -= 1
            if right + 1 < n:
                diff[right + 1] += 1
        s = 0
        for i in range(n):
            s += diff[i]
            if s + nums[i] > 0:
                # Check if the current value in nums[i] can be reduced to zero
                # > 0 means cannot
                return False
        return True
