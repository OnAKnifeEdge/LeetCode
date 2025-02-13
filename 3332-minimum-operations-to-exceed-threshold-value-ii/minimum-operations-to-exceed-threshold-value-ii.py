class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(heap:=[n for n in nums if n < k])
        cnt = 0
        while len(heap) > 1:
            cnt += 1
            x = 2 * heappop(heap) + heappop(heap)
            if x < k:
                heappush(heap, x)
            else:
                break

        return cnt + (len(heap) + 1) // 2