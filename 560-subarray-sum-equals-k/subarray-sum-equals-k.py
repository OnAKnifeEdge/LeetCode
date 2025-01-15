class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        count = 0
        prefix_sum = 0
        d[0] = 1
        for i, num in enumerate(nums):
            prefix_sum += num
            target = prefix_sum - k
            if target in d:
                count += d[target]
            d[prefix_sum] += 1
        return count
    