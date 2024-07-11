class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = [False] * len(candies)
        for i, candy in enumerate(candies):
            result[i] = candy + extraCandies >= max_candies
        return result
