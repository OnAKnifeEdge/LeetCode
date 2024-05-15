class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = [False] * len(nums)
        result = []
        for num in nums:
            if not seen[num - 1]:
                seen[num - 1] = True
            else:
                result.append(num)
        return result
