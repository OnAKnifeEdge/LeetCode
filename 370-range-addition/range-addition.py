class Difference:
    def __init__(self, nums: List[int]):
        assert len(nums) > 0
        self.diff = [0] * len(nums)
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i - 1]

    # 给闭区间 [i, j] 增加 val（可以是负数）
    def increment(self, i: int, j: int, val: int) -> None:
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val

    def result(self) -> List[int]:
        res = [0] * len(self.diff)
        # 根据差分数组构造结果数组
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = res[i - 1] + self.diff[i]
        return res

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:

        nums = [0] * length

        df = Difference(nums)
        
        for update in updates:
            i, j, val = update[0], update[1], update[2]
            df.increment(i, j, val)
        
        return df.result()


        