import bisect


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False

        window = sorted([])  # This will be our sorted window

        for i in range(len(nums)):
            num = nums[i]

            # Use bisect_left to find the insertion point for nums[i] in the window
            p = bisect.bisect_left(window, num)

            # Check for the ceiling (the next larger element or equal)
            if p < len(window) and window[p] - num <= t:
                return True

            # Check for the floor (the next smaller element)
            if p > 0 and num - window[p - 1] <= t:
                return True

            # Add the current element to the window
            bisect.insort(window, num)

            # Keep the window size fixed to k
            if len(window) > k:
                # Remove the element that is now out of the window
                window.remove(nums[i - k])

        return False
