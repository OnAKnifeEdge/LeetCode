class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        n = len(data)
        left = 0
        right = 0
        ones_in_window = 0
        max_ones_in_window = 0
        while right < n:
            ones_in_window += data[right]
            if right - left == ones:
                ones_in_window -= data[left]
                left += 1
            max_ones_in_window = max(max_ones_in_window, ones_in_window)
            right += 1
        return ones - max_ones_in_window
