class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # 1, 2, 3, 4
        # 5

        full_rounds = time // (n - 1)

        extra_time = time % (n - 1)
        # print(full_rounds, extra_time)

        if full_rounds % 2 == 0:
            return extra_time + 1
        else:
            return n - extra_time
