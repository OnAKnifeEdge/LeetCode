class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        products.sort()
        start, end = 0, len(products) - 1
        result = [[] for _ in range(len(searchWord))]

        for i, c in enumerate(searchWord):
            c = searchWord[i]

            while start <= end and (
                len(products[start]) <= i or products[start][i] != c
            ):
                start += 1
            while start <= end and (len(products[end]) <= i or products[end][i] != c):
                end -= 1

            for k in range(start, min(end + 1, start + 3)):
                result[i].append(products[k])

        return result
