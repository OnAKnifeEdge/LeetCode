class Pair:
    def __init__(self, idx1, idx2, nums1, nums2):
        self.idx1 = idx1
        self.idx2 = idx2
        self.nums1 = nums1
        self.nums2 = nums2
        self.sum = nums1[idx1] + nums2[idx2]

    def __lt__(self, other):
        return self.sum < other.sum


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []
        """
        nums1 = [1,7,11], nums2 = [2,4,6]
        组合出的所有数对儿这就可以抽象成三个有序链表：

        [1, 2] -> [1, 4] -> [1, 6] 
        [7, 2] -> [7, 4] -> [7, 6]
        [11, 2] -> [11, 4] -> [11, 6]

        let's start with heads [[1, 2], [7, 2], [11, 2]] first

        like leetcode 23: merge the lists and find the top k pairs
        """
        min_heap = []

        for i in range(min(k, len(nums1))):
            heappush(min_heap, Pair(i, 0, nums1, nums2))

        pairs = []
        while min_heap and len(pairs) < k:
            pair = heappop(min_heap)
            idx1, idx2 = pair.idx1, pair.idx2
            pairs.append([nums1[idx1], nums2[idx2]])

            if idx2 + 1 < len(nums2):
                heappush(min_heap, Pair(idx1, idx2 + 1, nums1, nums2))

        return pairs
