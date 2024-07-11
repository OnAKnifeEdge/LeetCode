class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        min_idx = None
        max_idx = None
        start = 0

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                start = i + 1
            if num == minK:
                min_idx = i
            if num == maxK:
                max_idx = i
            if min_idx is not None and max_idx is not None:
                if min_idx >= start and max_idx >= start:
                    count += min(min_idx, max_idx) - start + 1

        return count
