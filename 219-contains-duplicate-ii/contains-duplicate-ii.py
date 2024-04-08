class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums:
            return True
        if len(nums) > 1 and k == 0:
            return False
        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            s.add(nums[i])
            if len(s) == k + 1:
                s.remove(nums[i-k])
        return False