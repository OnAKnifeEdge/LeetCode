class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.i = 0  # 2D list row pointer
        self.j = 0  # 2D list column pointer

    def next(self) -> int:
        if not self.hasNext():
            return -1
        val = self.vec[self.i][self.j]
        self.j += 1  # move column pointer one step to the right
        return val

    def hasNext(self) -> bool:
        while self.i < len(self.vec) and self.j == len(self.vec[self.i]):
            self.i += 1  # move to the next non-empty row
            self.j = 0  # reset column pointer to 0
        return self.i < len(self.vec)  # check if there are any rows left
