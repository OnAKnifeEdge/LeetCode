class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        left, right = 0, len(height) - 1
        l_max, r_max = 0, 0

        while left < right:
            left_height, right_height = height[left], height[right]
            l_max = max(left_height, l_max)
            r_max = max(right_height, r_max)
            area = min(l_max, r_max) * (right - left)
            water = max(water, area)
            if left_height <= right_height:
                left += 1
            else:
                right -= 1
        return water
