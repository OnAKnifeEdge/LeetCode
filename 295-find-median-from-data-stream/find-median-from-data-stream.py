from heapq import heappop, heappush


class MedianFinder:

    def __init__(self):
        # heap pop min
        self.smaller = []  # * -1: min will be the max
        self.bigger = []

    def addNum(self, num: int) -> None:
        # always push to smaller
        if len(self.smaller) == 0 or num < -self.smaller[0]:
            heappush(self.smaller, -num)
        else:
            heappush(self.bigger, num)

        if len(self.smaller) < len(self.bigger):
            heappush(self.smaller, -heappop(self.bigger))
        if len(self.smaller) - len(self.bigger) == 2:
            heappush(self.bigger, -heappop(self.smaller))

    def findMedian(self) -> float:
        if len(self.smaller) > len(self.bigger):
            return -self.smaller[0]

        return (self.bigger[0] - self.smaller[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
