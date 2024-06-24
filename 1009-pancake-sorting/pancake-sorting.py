class Solution:
    def pancakeSort(self, cakes: List[int]) -> List[int]:
        result = []

        def reverse(i: int, j: int) -> None:
            while i < j:
                cakes[i], cakes[j] = cakes[j], cakes[i]
                i += 1
                j -= 1

        def sort(n: int) -> None:
            if n == 1:
                return

            idx = cakes.index(max(cakes[:n]))

            reverse(0, idx)
            result.append(idx + 1)

            reverse(0, n - 1)
            result.append(n)

            sort(n - 1)

        sort(len(cakes))

        return result
