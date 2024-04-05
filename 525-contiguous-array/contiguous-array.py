class Solution:
    def findMaxLength(self, nums: List[int]) -> int:     
        d = {}
        result = 0
        diff = 0

        for idx, num in enumerate(nums):
            diff += 1 if num else -1 # when num is 1 increment when num is 0 decrement

            if diff == 0:
                result = max(result, idx + 1)
            elif diff in d:
                result = max(result, idx - d[diff])
            else:
                d[diff] = idx

        return result


        # # generator https://leetcode.com/problems/contiguous-array/solutions/4883501/97-90-short-and-clear-with-generator-of-cumulated-differences
        # def findMaxLength(self, nums: List[int]) -> int:
        #     def cumulated_diffs():
        #         diff = 0
        #         for num in nums:
        #             yield diff
        #             diff += 1 if num else -1
        #         yield diff

        #     d = {}
        #     result = 0
        #     for idx, diff in enumerate(cumulated_diffs()):
        #         if diff in d:
        #             result = max(result, idx - d[diff])
        #         else:
        #             d[diff] = idx

        #     return result