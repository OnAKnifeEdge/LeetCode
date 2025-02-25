class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        count = 0
        prefix_sum = 0

        odd_count = 0
        even_count = 1  # sum(0) is even

        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 0:
                even_count += 1
                count += odd_count
            else:
                odd_count += 1
                count += even_count

            count %= MOD
        return count
