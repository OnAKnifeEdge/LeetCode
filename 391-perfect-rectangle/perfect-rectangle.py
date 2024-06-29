class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        if not rectangles:
            return False

        def get_area(i1, j1, i2, j2):
            a = abs(i2 - i1)
            b = abs(j2 - j1)
            return a * b

        x1, y1, x2, y2 = rectangles[0]
        area_sum = 0

        corner_set = set()

        for a1, b1, a2, b2 in rectangles:
            x1 = min(x1, a1)
            x2 = max(x2, a2)
            y1 = min(y1, b1)
            y2 = max(y2, b2)
            area_sum += get_area(a1, b1, a2, b2)

            # Add and remove corners to check for overlaps
            for x, y in [(a1, b1), (a2, b1), (a1, b2), (a2, b2)]:
                if (x, y) in corner_set:
                    corner_set.remove((x, y))
                else:
                    corner_set.add((x, y))

        # 左下，右上，左上，左下
        expected_corners = {(x1, y1), (x2, y2), (x1, y2), (x2, y1)}

        area = get_area(x1, y1, x2, y2)

        return area_sum == area and corner_set == expected_corners
