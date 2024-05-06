class Solution:
    # bidirectional bfs
    def openLock(self, deadends: List[str], target: str) -> int:
        # A helper function to get all possible combinations from the current state
        def neighbors(state: str) -> List[str]:
            for i in range(4):
                digit = int(state[i])
                for move in (-1, 1):
                    new_digit = (digit + move) % 10
                    yield state[:i] + str(new_digit) + state[i + 1:]

        # Helper method to expand the BFS from one side
        def expand(
            q: Deque[Tuple[str, int]],
            v: Dict[str, int],
            vv: Dict[str, int],
            no: Set[str],
        ) -> int:
            for _ in range(len(q)):
                current, turn = q.popleft()
                if current in vv:
                    # If current exists in the other visited, 
                    # that means we found an intersection.
                    # Total turns are the sum of turns from both sides + 1
                    return turn + vv[current]
                for next_state in neighbors(current):
                    if next_state not in v and next_state not in no:
                        # Keep searching, add next_state to visited and q
                        v[next_state] = turn + 1
                        q.append((next_state, turn + 1))
            return -1

        no = set(deadends)
        if target in no or "0000" in no:
            return -1

        # Initial state with turn counts
        visited_start, visited_target = {"0000": 0}, {target: 0}
        q1, q2 = deque([("0000", 0)]), deque([(target, 0)])

        while q1 and q2:
            from_start = expand(q1, visited_start, visited_target, no)
            if from_start != -1:
                return from_start

            from_target = expand(q2, visited_target, visited_start, no)
            if from_target != -1:
                return from_target

        return -1

    # one direction bfs
    # def openLock_bfs(self, deadends: List[str], target: str) -> int:

    #     no = set(deadends)
    #     visited = set("0000")
    #     q = deque([("0000", 0)])

    #     while q:

    #         current, turn = q.popleft()
    #         # 0000 (level 0)
    #         if current == target:
    #             return turn
    #         if current in no:
    #             visited.add((current, turn))
    #             continue
    #         # there are four digits
    #         for i in range(4):
    #             # 1000 9000 0100 0900 0010 0090 0001 0009 (level 1)
    #             # plus = self.plus_one(current, i)
    #             plus = self.rotate(current, i, 1)
    #             if plus not in visited and plus not in no:
    #                 q.append((plus, turn + 1))
    #                 visited.add(plus)
    #             # minus = self.minus_one(current, i)
    #             minus = self.rotate(current, i, -1)
    #             if minus not in visited and minus not in no:
    #                 q.append((minus, turn + 1))
    #                 visited.add(minus)
    #     return -1

    # def plus_one(self, s, i) -> str:
    #     if s[i] == "9":
    #         return s[:i] + "0" + s[i + 1:]
    #     return s[:i] + chr(ord(s[i]) + 1) + s[i + 1:]

    # def minus_one(self, s, i) -> str:
    #     if s[i] == "0":
    #         return s[:i] + "9" + s[i + 1:]
    #     return s[:i] + chr(ord(s[i]) - 1) + s[i + 1:]

    # def rotate(self, s, i, direction) -> str:
    #     new_digit = (int(s[i]) + direction) % 10
    #     return s[:i] + str(new_digit) + s[i + 1:]
