class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglies = [1]
        # primes = [2, 3, 5] => [(2, 2, 0), (3, 3, 0), (5, 5, 0)]
        min_heap = [(prime, prime, 0) for prime in primes]

        while len(uglies) < n:
            next_ugly, prime, idx = heappop(min_heap)

            if next_ugly != uglies[-1]:
                uglies.append(next_ugly)

            heappush(min_heap, (uglies[idx] * prime, prime, idx + 1))

        return uglies[-1]
