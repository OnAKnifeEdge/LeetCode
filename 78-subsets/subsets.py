class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def backtrack(start, temp):
            result.append(temp[:])
            for i in range(start, n):
                temp.append(nums[i])
                backtrack(i + 1, temp)
                temp.pop()

        backtrack(0, [])
        return result
