class FirstUnique:

    def __init__(self, nums: List[int]):
        self.count = defaultdict(int)
        self.q = deque()
        for num in nums:
            self.count[num] += 1
            self.q.append(num)

    def showFirstUnique(self) -> int:
        if not self.q:
            return -1
        while self.q:
            val = self.q[0]
            if self.count[val] == 1:
                return val
            else:
                self.q.popleft()
        return -1

    def add(self, value: int) -> None:
        self.count[value] += 1
        self.q.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
