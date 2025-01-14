class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = None
        missing = None
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
            else:
                duplicate = idx + 1

        for i, num in enumerate(nums):
            if num > 0:
                missing = i + 1

        return [duplicate, missing]
