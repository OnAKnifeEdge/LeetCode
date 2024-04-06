class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {}
        prefix_sum = 0
        cnt = 0


        for i, num in enumerate(nums):
            prefix_sum += num
            mod = prefix_sum % k

            if mod == 0:
                cnt += 1

            if mod < 0:
                mod += k

            if mod in d:
                cnt += d[mod]
                
            d[mod] = d.get(mod, 0) + 1

        return cnt

        