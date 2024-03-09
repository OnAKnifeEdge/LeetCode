class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ROWS, COLS = len(mat), len(mat[0])

        def binary_search(row):
            lo, hi = 0, COLS - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if row[mid] == 1:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo


        heap = []
        for i, row in enumerate(mat):
            strength = binary_search(row)
            entry = (-strength, -i)
            if len(heap) < k or entry > heap[0]:
                heapq.heappush(heap, entry)
            if len(heap) > k:
                heapq.heappop(heap)
        indexes = []
        while heap:
            indexes.append(-heapq.heappop(heap)[1])
        return indexes[::-1]

        # heap = []
        # for i, row in enumerate(mat):
        #     strength = binary_search(row)
        #     entry = (-strength, i) # I didn't flip the "i" to negative because I thought it would won't affect the comparator
        #     if len(heap) < k or entry > heap[0]:
        #         heapq.heappush(heap, entry)
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # indexes = []
        # while heap:
        #     indexes.append(heapq.heappop(heap)[1])
        # return indexes[::-1]


           