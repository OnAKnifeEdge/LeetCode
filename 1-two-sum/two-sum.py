class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return None
        m = {}
        for i in range(len(nums)):
            candidate = target - nums[i]
            if candidate in m:
                return [i, m[candidate]]
            m[nums[i]] = i

        