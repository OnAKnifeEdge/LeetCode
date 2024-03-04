class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            width = right - left
            max_area = max(max_area, width * min(height[left], height[right]))
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return max_area
        