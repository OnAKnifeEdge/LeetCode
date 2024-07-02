class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        result = []
        for k, v in c1.items():
            count = min(v, c2.get(k, 0))
            if count == 0:
                continue
            result.extend([k] * count)

        return result
