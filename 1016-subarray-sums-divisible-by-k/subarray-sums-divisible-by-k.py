class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {}
        prefix_sum = 0
        cnt = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            # Calculate the mod, adjusting immediately for negative values
            mod = (prefix_sum % k + k) % k # handle the negative cases

            if mod == 0:
                cnt += 1

            # If we've seen this mod before, it contributes to additional subarrays
            if mod in d:
                cnt += d[mod]

            d[mod] = d.get(mod, 0) + 1

        return cnt

        