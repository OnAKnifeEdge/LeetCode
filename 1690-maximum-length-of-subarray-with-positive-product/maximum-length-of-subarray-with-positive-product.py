class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        positive_cnt = 0
        negative_cnt = 0

        max_length = 0

        for num in nums:
            if num > 0:
                positive_cnt += 1
                negative_cnt += 1 if negative_cnt else 0
            elif num < 0:
                positive_cnt_copy, negative_cnt_copy = positive_cnt, negative_cnt
                positive_cnt = negative_cnt_copy + 1 if negative_cnt else 0
                negative_cnt = positive_cnt_copy + 1
            else:
                positive_cnt = negative_cnt = 0

            max_length = max(max_length, positive_cnt)
        return max_length
