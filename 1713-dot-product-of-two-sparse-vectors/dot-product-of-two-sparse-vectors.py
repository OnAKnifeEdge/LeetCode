class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.vector[i] = num

    def get_vector(self):
        return self.vector

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        v1 = self.get_vector()
        v2 = vec.get_vector()

        if len(v1) > len(v2):
            v1, v2 = v2, v1

        product = 0

        for k1, v1 in v1.items():
            if k1 in v2:  # Simplified: check if key is present in v2
                product += v1 * v2[k1]

        return product


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
