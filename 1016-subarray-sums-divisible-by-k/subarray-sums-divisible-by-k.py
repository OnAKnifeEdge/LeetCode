class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        d = {}
        for i, num in enumerate(nums):
            prefix_sum += num
            mod = (prefix_sum % k + k) % k
            if mod == 0:
                count += 1
            if mod in d:
                count += d[mod]
                d[mod] += 1
            else:
                d[mod] = 1
        return count
