class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # https://leetcode.com/problems/longest-well-performing-interval/submissions/1224328300/
        # https://leetcode.com/problems/contiguous-array/description/
        # 325
        n = len(nums)
        prefix_mod = 0
        mod_seen = {0: -1}

        for i in range(n):
            prefix_mod = (prefix_mod + nums[i]) % k

            if prefix_mod not in mod_seen:
                mod_seen[prefix_mod] = i
            elif i - mod_seen[prefix_mod] >= 2:
                return True
        return False
