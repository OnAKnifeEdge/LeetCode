class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        l_max, r_max = 0, 0
        result = 0

        while left < right:
            left_height = height[left]
            right_height = height[right]
            if left_height <= right_height:
                l_max = max(left_height, l_max)
                result += l_max - left_height
                left += 1
            else:
                r_max = max(right_height, r_max)
                result += r_max - right_height
                right -= 1
        return result
