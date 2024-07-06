class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []
        for idx, val in enumerate(nums):
            if val != 0:
                self.pairs.append((idx, val))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        product = 0
        v1 = self.pairs
        v2 = vec.pairs
        i, j = 0, 0
        while i < len(v1) and j < len(v2):
            if v1[i][0] == v2[j][0]:
                product += v1[i][1] * v2[j][1]
                i += 1
                j += 1
            elif v1[i][0] < v2[j][0]:  # 1, 3
                i += 1
            else:
                j += 1
        return product


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
