class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for idx, num in enumerate(nums):
            if num in d and abs(idx - d[num]) <= k:
                return True

            d[num] = idx
        return False
