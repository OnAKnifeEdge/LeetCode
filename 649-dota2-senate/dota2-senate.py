class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D, R = deque(), deque()

        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)

        while D and R:
            d = D.popleft()
            r = R.popleft()
            if r < d:
                R.append(d + len(senate))
            else:
                D.append(r + len(senate))

        return "Radiant" if R else "Dire"