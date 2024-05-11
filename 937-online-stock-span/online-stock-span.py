class StockSpanner:
    # [7, 2, 1, 2]: 2 next larger number [2, 1, 2, 7]

    def __init__(self):
        self.mono_stack = []  # (price, cnt)

    def next(self, price: int) -> int:
        cnt = 1
        while self.mono_stack and self.mono_stack[-1][0] <= price:
            cnt += self.mono_stack.pop()[1]
        self.mono_stack.append((price, cnt))
        return cnt


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
