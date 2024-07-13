class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        pairs = []

        def binary_search(nums, target):
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                elif nums[mid] >= target:
                    hi = mid - 1
            return lo

        for spell in spells:
            min_potion = math.ceil(success / spell)
            # i = bisect_left(potions, min_potion)
            i = binary_search(potions, min_potion)
            pairs.append(len(potions) - i)

        return pairs
