class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq = []
        for i in range(len(matrix)):
            heapq.heappush(pq, (matrix[i][0], i, 0))
        
        while pq and k:
            num, i, j = heapq.heappop(pq)
            k -= 1
            if j + 1 < len(matrix[0]):
                heapq.heappush(pq, (matrix[i][j + 1], i, j + 1))

        return num

        