class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights = [h for _, h in envelopes]
        return self.lis(heights)

    def lis(self, nums):
        cards = []
        for num in nums:
            idx = bisect_left(cards, num)
            if idx == len(cards):
                cards.append(num)
            else:
                cards[idx] = num
        return len(cards)
