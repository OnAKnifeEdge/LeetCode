class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for idx, num in enumerate(nums):
            if idx > k:
                window.remove(nums[idx - k - 1])
            if num in window:
                return True
            window.add(num)
        return False
