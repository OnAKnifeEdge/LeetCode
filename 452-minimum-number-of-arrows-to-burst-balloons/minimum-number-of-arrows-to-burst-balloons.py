class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x: x[1])

        count = 0
        right = float("-inf")

        for x1, x2 in points:
            if x1 > right:
                right = x2
                count += 1
        return count
