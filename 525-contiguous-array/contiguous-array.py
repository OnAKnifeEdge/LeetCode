class Solution:
    # def findMaxLength(self, nums: List[int]) -> int:
        # zero, one = 0, 0
        # diff_map = {}
        # result = 0

        # for i, num in enumerate(nums):
        #     if num == 0:
        #         zero += 1
        #     elif num == 1:
        #         one += 1
            
        #     if one - zero not in diff_map:
        #         diff_map[one - zero] = i

        #     if one == zero:
        #         result = one + zero
        #     else:
        #         idx = diff_map.get(one - zero)
        #         result = max(result, i - idx)

        # return result

        # generator https://leetcode.com/problems/contiguous-array/solutions/4883501/97-90-short-and-clear-with-generator-of-cumulated-differences
        def findMaxLength(self, nums: List[int]) -> int:
            def cumulated_diffs():
                diff = 0
                for num in nums:
                    yield diff
                    diff += 1 if num else -1
                yield diff

            d = {}
            result = 0
            for idx, diff in enumerate(cumulated_diffs()):
                if diff in d:
                    result = max(result, idx - d[diff])
                else:
                    d[diff] = idx

            return result