class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food

        self.snake = collections.deque([(0, 0)])
        self.snake_set = {(0, 0)}

        self.score = 0
        self.movement = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    def move(self, direction: str) -> int:
        dx, dy = self.movement[direction]
        x, y = self.snake[0]
        xx, yy = x + dx, y + dy

        if xx < 0 or yy < 0 or xx >= self.height or yy >= self.width:
            return -1

        tail = self.snake[-1]

        if (xx, yy) in self.snake_set and (xx, yy) != tail:
            return -1

        if self.score < len(self.food) and tuple(self.food[self.score]) == (xx, yy):
            self.score += 1
        else:
            self.snake_set.remove(self.snake.pop())

        self.snake.appendleft((xx, yy))
        self.snake_set.add((xx, yy))

        return self.score
