class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # (val, row_idx, col_idx) for first column
        min_heap = [(row[0], i, 0) for i, row in enumerate(matrix) if row]
        heapify(min_heap)

        # result = []
        kth = 0
        while min_heap and k > 0:
            kth, i, j = heappop(min_heap)
            # result.append(kth)
            if j + 1 < len(matrix[0]):
                # move to the next column
                heappush(min_heap, (matrix[i][j + 1], i, j + 1))
            k -= 1
        # return result[k - 1]
        return kth
