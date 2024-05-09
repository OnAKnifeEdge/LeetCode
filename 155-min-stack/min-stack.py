class Pair(NamedTuple):
    val: int
    smallest: int


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(Pair(val=val, smallest=val))
        else:
            last_smallest = self.getMin()
            self.stack.append(Pair(val=val, smallest=min(val, last_smallest)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].smallest


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
