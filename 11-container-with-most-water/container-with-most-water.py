class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        l_max, r_max = float("-inf"), float("-inf")
        max_area = 0
        while i < j:
            left, right = height[i], height[j]
            l_max = max(left, l_max)
            r_max = max(right, r_max)
            area = min(l_max, r_max) * (j - i)
            max_area = max(max_area, area)

            if left <= right:
                i += 1
            else:
                j -= 1
        return max_area
