class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        numbers = [False, False] + [True] * (n - 2)

        for p in range(2, int(sqrt(n) + 1)):
            if numbers[p]:
                # There are ceil(n / p - p) numbers between p*p and n that are multiples of p.
                numbers[p * p : n : p] = [False] * math.ceil(n/p - p)

        return sum(numbers)
        
        