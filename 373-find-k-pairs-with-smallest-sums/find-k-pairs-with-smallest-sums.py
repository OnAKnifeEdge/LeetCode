class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        pq = []
        for i in range(len(nums1)):
            heapq.heappush(pq, (nums1[i] + nums2[0],i, 0))

        answer = []

        while pq and k > 0:
            k -= 1
            s, i, j = heapq.heappop(pq)

            if j + 1 < len(nums2):
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))

            p = [nums1[i], nums2[j]]
            answer.append(p)
        return answer
