class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, one = 0, 0
        diff_map = {}
        result = 0

        for i, num in enumerate(nums):
            if num == 0:
                zero += 1
            elif num == 1:
                one += 1
            
            if one - zero not in diff_map:
                diff_map[one - zero] = i

            if one == zero:
                result = one + zero
            else:
                idx = diff_map.get(one - zero)
                result = max(result, i - idx)

        return result


        







        # generator https://leetcode.com/problems/contiguous-array/solutions/4883501/97-90-short-and-clear-with-generator-of-cumulated-differences
        # def findMaxLength(self, nums: List[int]) -> int:
        #     def cumulated_diffs():
        #         prev = 0
        #         for num in nums:
        #             yield prev
        #             prev += 1 if num else -1
        #         yield prev

        #     dct = {}
        #     ans = 0
        #     for ind, dif in enumerate(cumulated_diffs()):
        #         if dif in dct:
        #             if ans < ind - dct[dif]:
        #                 ans = ind - dct[dif]
        #         else:
        #             dct[dif] = ind

        #     return ans