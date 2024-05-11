class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # find the next smaller or equal number
        n = len(prices)
        discounts = [0] * n
        mono_stack = []

        for i in reversed(range(n)):
            # mono_stack 里的都不大于 prices[i]
            while mono_stack and mono_stack[-1] > prices[i]:
                mono_stack.pop()
            discounts[i] = prices[i] - mono_stack[-1] if mono_stack else prices[i]
            mono_stack.append(prices[i])

        return discounts
