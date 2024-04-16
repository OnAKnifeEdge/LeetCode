class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.d = {}
        blacklist_set = set(blacklist)
        self.l = n - len(blacklist)

        last = n - 1
        for b in blacklist:
            if b >= self.l: # If 'b' is not affecting the range [0, self.l), ignore it.
                continue
            
            while last in blacklist_set:
                last -= 1  # Decrease 'last' until it's not in the blacklist.
            self.d[b] = last # Map 'b' to the 'last' non-blacklisted value.
            last -= 1 # Prepare 'last' for the potential next mapping.

    def pick(self) -> int:
        k = random.randint(0, self.l - 1) # Generate a random index in the allowed range.
        return self.d.get(k, k) # Return the remapped value if 'k' is blacklisted, otherwise 'k' itself.
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()