class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] += 1
        sneaky = []
        for i, num in enumerate(nums):
            idx = abs(num)
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
            else:
                sneaky.append(idx - 1)
        return sneaky
