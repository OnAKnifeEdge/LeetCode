class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        d = {}
        result = 0
        diff = 0

        for i, hour in enumerate(hours):
            diff += 1 if hour > 8 else -1

            if diff > 0: # well-performing
                result = max(result, i + 1)
            else:
                if diff not in d:
                    d[diff] = i
                if diff - 1 in d:
                    result = max(result, i - d[diff - 1])

        return result

        