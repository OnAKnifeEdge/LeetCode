class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numbers = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        for i, num in enumerate(nums):
            if num > 0:
                numbers.append(i + 1)
        return numbers
