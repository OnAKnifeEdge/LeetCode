class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_sum = -1
        lookup = [0] * 82

        def calculate_digit_sum(num):
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10
            return digit_sum

        for num in nums:
            digit_sum = calculate_digit_sum(num)
            if lookup[digit_sum] > 0:
                max_sum = max(max_sum, lookup[digit_sum] + num)

            lookup[digit_sum] = max(lookup[digit_sum], num)

        return max_sum
