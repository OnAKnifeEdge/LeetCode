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

            # [3,2,4,1]
            reverse(0, idx)
            # [4,2,3,1]
            reverse(0, n - 1)
            # [1,3,2,4]
            result.append(idx + 1)
            result.append(n)

            sort(n - 1)

        sort(len(cakes))

        return result
