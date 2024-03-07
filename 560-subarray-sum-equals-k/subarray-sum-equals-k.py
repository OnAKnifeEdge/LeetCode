class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # https://leetcode.com/problems/subarray-sum-equals-k/solutions/3777004/why-sum-k-read-this-to-understand/
        # d[sum] -> OccuranceCount
        d = {0: 1}
        s, count = 0, 0
        for i, e in enumerate(nums):
            s += e
            if s - k in d:
                count += d[s - k]
            d[s] = d.get(s, 0) + 1
        return count

        