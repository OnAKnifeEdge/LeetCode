class Solution:
    def __init__(self, nums: List[int]):
        # save nums array for reservoir sampling for the first
        # call to pick
        self.nums = nums
        # save lists of indices to skip reservoir sampling
        # after we've done one pick
        self.indices = defaultdict(list)

    def pick(self, target: int) -> int:
        # if we've already called pick, just randomly select
        # from the saved index list
        if target in self.indices:
            return self.indices[target][randint(0, len(self.indices[target]) - 1)]

        # otherwise, iterate through the whole list for reservoir
        # sampling

        count = 0
        idx = -1

        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                if random.randint(1, count) == 1:
                    idx = i
                self.indices[num].append(i)
        return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
