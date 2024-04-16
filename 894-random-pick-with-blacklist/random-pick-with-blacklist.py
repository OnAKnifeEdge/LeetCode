class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.d = {}
        blacklist_set = set(blacklist)
        self.l = n - len(blacklist)

        last = n - 1
        for b in blacklist:
            if b >= self.l:
                continue
            
            while last in blacklist_set:
                last -= 1
            self.d[b] = last
            last -= 1

    def pick(self) -> int:
        k = random.randint(0, self.l - 1)
        return self.d.get(k, k)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()