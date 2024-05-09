class Logger:

    def __init__(self):
        self.set = set()
        self.q = deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.q:
            msg, ts = self.q[0]
            if timestamp - ts < 10:
                break
            self.q.popleft()
            self.set.remove(msg)

        if message not in self.set:
            self.set.add(message)
            self.q.append((message, timestamp))
            return True

        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
