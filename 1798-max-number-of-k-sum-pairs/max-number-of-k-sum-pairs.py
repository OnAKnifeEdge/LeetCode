class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        d = defaultdict(int)
        for num in nums:
            if k - num in d:
                count += 1
                d[k - num] -= 1
                if d[k - num] == 0:
                    del d[k - num]
            else:
                d[num] += 1
        return count
