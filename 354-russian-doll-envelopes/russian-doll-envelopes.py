class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))  # sort by width asc and height desc
        heights = [h for w, h in envelopes]

        def lis(nums):
            sub = []
            for num in nums:
                idx = bisect_left(sub, num)
                if idx == len(sub):
                    sub.append(num)
                sub[idx] = num
            return len(sub)

        return lis(heights)
