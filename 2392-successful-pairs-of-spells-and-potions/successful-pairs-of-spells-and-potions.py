class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # return (len(potions) - bisect_left(potions, success, key=lambda p: p * s) for s in spells)

        potions.sort()
        answer = []

        max_potion = potions[- 1]
        for spell in spells:
            min_potion = math.ceil(success/spell)
            i = bisect_left(potions, min_potion)
            answer.append(len(potions) - i)
        return answer

        