class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []

        d = {}

        for i, num in enumerate(nums):
            if target - num in d:
                return [i, d[target - num]]
            else:
                d[num] = i
        return []
