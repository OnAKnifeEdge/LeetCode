class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gain = [g - c for g, c in zip(gas, cost)]

        if sum(gain) < 0:
            return -1

        total_gain, start = 0, 0
        for i, g in enumerate(gain):
            total_gain += g

            if total_gain < 0:
                start = i + 1
                total_gain = 0

        return start
