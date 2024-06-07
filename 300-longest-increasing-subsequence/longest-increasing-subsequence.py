class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cards = []
        for num in nums:
            idx = bisect_left(cards, num)
            if idx == len(cards):
                cards.append(num)
            else:
                cards[idx] = num
        return len(cards)
