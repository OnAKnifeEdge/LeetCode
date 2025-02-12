class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_sum = -1
        lookup = defaultdict(list)

        def calculate_digit_sum(num):
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10
            return digit_sum

        for num in nums:
            digit_sum = calculate_digit_sum(num)
            heappush(lookup[digit_sum], num)
            if len(lookup[digit_sum]) > 2:
                heappop(lookup[digit_sum])

        for max_heap in lookup.values():
            if len(max_heap) == 2:
                a = heappop(max_heap)
                b = heappop(max_heap)
                max_sum = max(max_sum, a + b)
        return max_sum
