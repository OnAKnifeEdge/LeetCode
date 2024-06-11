class Solution:

    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_dict = defaultdict(list)

        for i, c in enumerate(ring):
            ring_dict[c].append(i)

        r, k = len(ring), len(key)

        dp = [[float("inf")] * (k + 1) for _ in range(r)]
        # dp[i][j] means: ring[i], key[j:]

        for i in range(r):
            dp[i][k] = 0

        for j in reversed(range(k)):
            for i in range(r):
                for idx in ring_dict[key[j]]:
                    diff = abs(idx - i)
                    steps = min(diff, r - diff)
                    dp[i][j] = min(dp[i][j], 1 + steps + dp[idx][j + 1])

        return dp[0][0]

    # class Solution:
    #     def findRotateSteps(self, ring: str, key: str) -> int:
    #         ring_dict = defaultdict(list)

    #         for i, c in enumerate(ring):
    #             ring_dict[c].append(i)

    #         r, k = len(ring), len(key)

    #         # Initialize a large integer but within reasonable bounds, to replace float("inf").
    #         max_steps = r * k * 2
    #         dp = [[max_steps] * (k + 1) for _ in range(r)]

    #         # Base cases: no steps needed after the last character of the key has been spelled out.
    #         for i in range(r):
    #             dp[i][k] = 0

    #         # Fill in the DP table from the last character of the key working towards the first
    #         for j in reversed(range(k)):  # For each character in the key
    #             for i in range(r):  # For each position of the ring
    #                 for idx in ring_dict[
    #                     key[j]
    #                 ]:  # For each position where key character appears in the ring
    #                     # Calculate the number of steps to rotate from position 'i' to 'idx'
    #                     diff = abs(idx - i)
    #                     steps = min(diff, r - diff)  # Clockwise or counterclockwise
    #                     # Update the DP table: Consider rotation steps, button press (+1), and remaining cost.
    #                     dp[i][j] = min(dp[i][j], 1 + steps + dp[idx][j + 1])

    #         # Calculate minimum steps needed from starting position to spell out all characters
    #         # We also add the number of step presses for each character in the key.
    #         return dp[0][0]

    def findRotateSteps_topdown(self, ring: str, key: str) -> int:
        # Create a dictionary mapping each character in the ring to its indexes
        ring_dict = defaultdict(list)
        for i, c in enumerate(ring):
            ring_dict[c].append(i)

        # 计算圆盘指针在 ring[i]，输入 key[j..] 的最少操作数
        @lru_cache(maxsize=None)
        def dp(i, j):
            # If we have processed the entire key, no more steps are needed
            if j == len(key):
                return 0

            n = len(ring)
            # Initialize the minimum number of steps to a large number
            min_steps = float("inf")

            # Iterate through all the positions of the current key character in the ring
            for k in ring_dict[key[j]]:
                steps = min(abs(k - i), n - abs(k - i))

                # Add the rotation steps for remaining characters
                min_steps = min(min_steps, steps + dp(k, j + 1) + 1)

            return min_steps

        return dp(0, 0)
