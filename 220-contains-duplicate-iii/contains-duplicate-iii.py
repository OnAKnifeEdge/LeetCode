class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        if valueDiff < 0:
            return False

        window = sorted([])

        for idx, num in enumerate(nums):
            start = bisect.bisect_left(window, num)
            # [0, 1, 2, 4], 3 start is idx = 3 (value = 4)
            # window[start] >= num
            # Check for the ceiling (the next bigger element)
            if start < len(window) and window[start] - num <= valueDiff:
                return True

            # Check for the floor (the next smaller element)
            if start > 0 and num - window[start - 1] <= valueDiff:
                return True

            # Add the current element to the window
            bisect.insort(window, num)

            # Keep the window size fixed to indexDiff
            if len(window) > indexDiff:
                # Remove the element that is now out of the window
                window.remove(nums[idx - indexDiff])

        return False
