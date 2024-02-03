from collections import deque
from typing import List


class MyQueue:

    def __init__(self):
        self.q = deque([])
        self.max_q = deque([])

    def push(self, x):
        self.q.append(x)
        while self.max_q:
            left = self.max_q[-1]
            if x > left:
                self.max_q.pop()
            else:
                break
        self.max_q.append(x)

    def pop(self):
        x = self.q.popleft()
        if x == self.max_q[0]:
            self.max_q.popleft()
        return x

    def max(self):
        return self.max_q[0]

    def empty(self):
        return len(self.q) == 0


s = MyQueue()
t = [1, 2, 3, 4, 5]
for i in t:
    s.push(i)
    print(s.max())
    print(s.empty())

print('====')
for i in t:
    print('max', s.max())
    print(s.pop())
    print(s.empty())


class Solution:
    def three_consecutive_odds(self, arr: List[int]) -> bool:
        index = 0
        while index <= len(arr) - 3:
            a = arr[index]
            b = arr[index + 1]
            c = arr[index + 2]
            if a % 2 == 1 and b % 2 == 1 and c % 2 == 1:
                return True
            index = index + 1
        return False

    def min_operations(self, n: int) -> int:
        # if odd, 加一半
        # if even, 加一半但是是偶数的
        # 项数是 n//2
        if n <= 1:
            return 0
        if n == 2:
            return 1
        c = n // 2
        # n=6, arr=[1,3,5,7,9,11]，那么我们发现对1和11操作5次，再对3和9操作3次，再对5和7操作1次，就变成了[6]*n，所以答案是1+3+5=8
        if n % 2 == 0:
            start = 1
            end = c * 2 - 1
        else:
            start = 2
            end = n // 2 * 2
        return (start + end) * c // 2


if __name__ == '__main__':
    solution = Solution()
    # inp = [2, 6, 4, 1]
    # print(solution.three_consecutive_odds(inp))
    # inp = [1, 2, 1, 1]
    # print(solution.three_consecutive_odds(inp))

    solution.min_operations(6)
