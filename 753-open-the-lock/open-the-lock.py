class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        no = set(deadends)
        step = 0

        def plus_one(code, i):
            c = code[i]
            val = int(c)
            if val == 9:
                return code[:i] + '0' + code[i+1:]
            return code[:i] + str(val + 1) + code[i+1:]

        def minus_one(code, i):
            c = code[i]
            val = int(c)
            if val == 0:
                return code[:i] + '9' + code[i+1:]
            return code[:i] + str(val - 1) + code[i+1:]

        q = deque(["0000"])
        visited = {"0000"}
        while q:
            n = len(q)
            for i in range(n):
                code = q.popleft()
                if code in no:
                    continue
                if code == target:
                    return step
                for j in range(4):
                    up = plus_one(code, j)
                    down = minus_one(code, j)
                    if up not in visited:
                        q.append(up)
                        visited.add(up)
                    if down not in visited:
                        q.append(down)
                        visited.add(down)
            step += 1

        return -1
