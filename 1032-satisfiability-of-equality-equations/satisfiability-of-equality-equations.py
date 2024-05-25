class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = list(range(26))

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for e in equations:
            a, sign, _, b = list(e)
            if sign == "=":
                x, y = ord(a) - ord("a"), ord(b) - ord("a")
                union(x, y)

        for e in equations:
            a, sign, _, b = list(e)
            if sign == "!":
                x, y = ord(a) - ord("a"), ord(b) - ord("a")
                if find(x) == find(y):
                    return False
        return True
