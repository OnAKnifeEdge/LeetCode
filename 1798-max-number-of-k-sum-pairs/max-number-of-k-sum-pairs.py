class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        d = defaultdict(int)
        for num in nums:
            if d[k - num] > 0:
                count += 1
                d[k - num] -= 1
            else:
                d[num] += 1
        return count
