class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums:
            return True
        if len(nums) > 1 and k == 0:
            return False
        window = set()

        for idx, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)
            if len(window) == k + 1:
                window.remove(nums[idx - k])
        return False
