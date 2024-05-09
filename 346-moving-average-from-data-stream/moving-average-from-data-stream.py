class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.q.append(val)
        eviction = 0
        if len(self.q) > self.size:
            eviction = self.q.popleft()
        self.window_sum = self.window_sum + val - eviction
        return self.window_sum / min(len(self.q), self.size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
