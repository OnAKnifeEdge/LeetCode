class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_mod = 0
        d = defaultdict(int)
        d[0] = 1
        for num in nums:
            prefix_mod = (prefix_mod + num) % k
            if prefix_mod < 0:
                prefix_mod += k
            count += d[prefix_mod]
            d[prefix_mod] += 1
        return count
