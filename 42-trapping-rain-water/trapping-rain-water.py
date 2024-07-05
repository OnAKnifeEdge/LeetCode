class Solution:
    def trap(self, height: List[int]) -> int:
        l_max, r_max = 0, 0
        i, j = 0, len(height) - 1
        result = 0
        while i < j:
            left = height[i]
            right = height[j]

            if left <= right:
                l_max = max(l_max, left)
                result += l_max - left
                i += 1
            else:
                r_max = max(r_max, right)
                result += r_max - right
                j -= 1

        return result
