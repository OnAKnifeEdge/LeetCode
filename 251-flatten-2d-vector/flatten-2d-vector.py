class Vector2D:

    def __init__(self, vec: List[List[int]]):
        def generator():
            for row in vec:
                for c in row:
                    yield c

        self._generator = generator()
        self._next = next(self._generator, None)

    def next(self) -> int:
        nxt = self._next
        self._next = next(self._generator, None)
        return nxt

    def hasNext(self) -> bool:
        return self._next is not None


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
