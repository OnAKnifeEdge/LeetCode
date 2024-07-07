class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = "123456789"
        nums = []

        m, n = len(str(low)), len(str(high))
        # Input: low = 1000, high = 13000
        # (4, 5)
        # Output: [1234,2345,3456,4567,5678,6789,12345]
        for window in range(m, n + 1):
            for i in range(10 - window):
                num = int(sample[i:i + window])
                if low <= num <= high:
                    nums.append(num)
        return nums
