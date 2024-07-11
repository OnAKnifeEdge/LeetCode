class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        left_max, right_max = 0, 0
        max_area = 0
        while i < j:
            left_max = max(left_max, height[i])
            right_max = max(right_max, height[j])
            area = min(left_max, right_max) * (j - i)
            max_area = max(area, max_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area
