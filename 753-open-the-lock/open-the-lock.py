class Solution:

    def plus_one(self, s, i) -> str:
        if s[i] == "9":
            return s[:i] + "0" + s[i + 1:]
        return s[:i] + chr(ord(s[i]) + 1) + s[i + 1:]

    def minus_one(self, s, i) -> str:
        if s[i] == "0":
            return s[:i] + "9" + s[i + 1:]
        return s[:i] + chr(ord(s[i]) - 1) + s[i + 1:]

    def openLock(self, deadends: List[str], target: str) -> int:

        no = set(deadends)
        visited = set("0000")
        q = deque([("0000", 0)])

        while q:

            current, turn = q.popleft()
            # 0000 (level 0)
            if current == target:
                return turn
            if current in no:
                visited.add((current, turn))
                continue
            # there are four digits
            for i in range(4):
                # 1000 9000 0100 0900 0010 0090 0001 0009 (level 1)
                plus = self.plus_one(current, i)
                if plus not in visited and plus not in no:
                    q.append((plus, turn + 1))
                    visited.add(plus)
                minus = self.minus_one(current, i)
                if minus not in visited and minus not in no:
                    q.append((minus, turn + 1))
                    visited.add(minus)
        return -1
