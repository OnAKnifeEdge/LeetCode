class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for idx, num in enumerate(nums):
            if num in d:
                if abs(idx - d[num]) <= k:
                    return True
                else:
                    d[num] = idx
            else:
                d[num] = idx
        return False
