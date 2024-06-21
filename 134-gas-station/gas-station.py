class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        s = sum(gas) - sum(cost)
        if s < 0:
            return -1

        total_gain, start = 0, 0
        for i in range(len(gas)):
            total_gain += gas[i] - cost[i]

            if total_gain < 0:
                start = i + 1
                total_gain = 0

        return start
