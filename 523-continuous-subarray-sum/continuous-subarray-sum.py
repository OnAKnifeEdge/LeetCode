class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # https://leetcode.com/problems/longest-well-performing-interval/submissions/1224328300/
        # https://leetcode.com/problems/contiguous-array/description/
        # 325
        d = {}
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            mod_k = prefix_sum % k
            if mod_k == 0 and i > 0:
               return True

            if mod_k not in d:
                d[mod_k] = i

            if mod_k in d and i - d[mod_k] > 1:
                return True

        return False
