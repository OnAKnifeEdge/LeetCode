class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(a, b) for a, b in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda p:p[1], reverse=True)
        max_score = 0
        min_heap = []
        prefix_sum = 0
        for a, b in pairs:
            prefix_sum += a
            heapq.heappush(min_heap, a)
            if len(min_heap) == k:
                max_score = max(max_score, b * prefix_sum)
                prefix_sum -= heapq.heappop(min_heap)
        return max_score
