class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        result = []
        m, n = len(firstList), len(secondList)
        i, j = 0, 0
        while i < m and j < n:
            left1, right1 = firstList[i]
            left2, right2 = secondList[j]
            # 无交集
            if right1 < left2:
                i += 1
                continue
            # 无交集
            if right2 < left1:
                j += 1
                continue
            # 有交集
            start = max(left1, left2)
            end = min(right1, right2)
            result.append((start, end))

            if right2 < right1:
                j += 1
            else:
                i += 1

        return result
