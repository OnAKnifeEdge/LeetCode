class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        frequency = [0] * (len(A) + 1)
        prefix = []
        count = 0
        for a, b in zip(A, B):
            frequency[a] += 1
            if frequency[a] == 2:
                count += 1
            frequency[b] += 1
            if frequency[b] == 2:
                count += 1
            prefix.append(count)
        return prefix
