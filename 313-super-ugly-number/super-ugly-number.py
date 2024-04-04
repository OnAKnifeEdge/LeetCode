class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        q = [1]
        while n > 1: 
            n -= 1
            num = heapq.heappop(q)
            for prime in primes:
                heapq.heappush(q, prime * num)
                if num % prime == 0:
                    break
        return q[0]