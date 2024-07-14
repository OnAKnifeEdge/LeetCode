class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in reversed(range(len(temperatures))):
            temperature = temperatures[i]
            while stack and temperature >= stack[-1][0]:
                stack.pop()
            if stack:
                result[i] = stack[-1][1] - i
            stack.append((temperature, i))
        return result
