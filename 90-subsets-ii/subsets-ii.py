class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)

        def backtrack(current, start):
            result.append(current[:])

            for i in range(start, n):
                # if i > 0 and nums[i] == nums[i - 1]: BUG
                if i > start and nums[i] == nums[i - 1]:
                    continue
                current.append(nums[i])
                backtrack(current, i + 1)
                current.pop()

        backtrack([], 0)
        return result
        