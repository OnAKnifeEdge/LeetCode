class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque()
        self.count = defaultdict(int)
        for num in nums:
            self.q.append(num)
            self.count[num] += 1

    def showFirstUnique(self) -> int:
        if not self.q:
            return -1
        while self.q:
            val = self.q[0]
            if self.count[val] == 1:  # first unique number:
                return val
            else:
                self.q.popleft()
        return -1

    def add(self, value: int) -> None:
        self.q.append(value)
        self.count[value] += 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
