class UnionFind:

    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
        self.count = [1] * size  # Store the size of each component

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:  # x is smaller
            self.parent[root_x] = root_y
            self.count[root_y] += self.count[root_x]
        elif self.rank[root_x] > self.rank[root_y]:  # y is smaller
            self.parent[root_y] = root_x
            self.count[root_x] += self.count[root_y]
        else:
            self.parent[root_y] = root_x
            self.count[root_x] += self.count[root_y]
            self.rank[root_x] += 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        n = len(nums_set)
        uf = UnionFind(n)

        idx = {num: i for i, num in enumerate(nums_set)}

        for num in nums_set:
            if num - 1 in nums_set:
                uf.union(idx[num - 1], idx[num])
            if num + 1 in nums_set:
                uf.union(idx[num + 1], idx[num])

        return max(uf.count)
