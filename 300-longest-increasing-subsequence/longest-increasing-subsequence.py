class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:  # increasing
        #             dp[i] = max(dp[j] + 1, dp[i])
        # return max(dp)

        # binary search

        """
        Let's start with an empty sub list and go through the list [10, 9, 2, 5, 3, 7, 101, 18] step by step:
        num = 10, sub = [], so we append 10 to sub. Now, sub = [10].
        num = 9, sub = [10]. We find 9 should be inserted at index 0 in sub, replacing 10. Now, sub = [9].
        num = 2, sub = [9]. 2 should be inserted at index 0, replacing 9. Now, sub = [2].
        num = 5, sub = [2]. 5 is greater than 2, so we append 5 to sub. Now, sub = [2, 5].
        num = 3, sub = [2, 5]. 3 should be inserted at index 1, replacing 5. Now, sub = [2, 3].
        num = 7, sub = [2, 3]. 7 is greater than 3, so we append 7 to sub. Now, sub = [2, 3, 7].
        num = 101, sub = [2, 3, 7]. 101 is greater than 7, so we append 101 to sub. Now, sub = [2, 3, 7, 101].
        num = 18, sub = [2, 3, 7, 101]. 18 should be inserted at index 3, replacing 101. Now, sub = [2, 3, 7, 18].
        Finally, it returns len(sub) = 4, which is the length of the longest increasing subsequence ([2, 3, 7, 18]) in the given list. Here you can see that rather than preserving the actual longest subsequence, the code prioritizes maintaining the minimum possible tail element for each length of increasing subsequence, allowing future elements to extend the sequence further.
        """
        sub = []
        for num in nums:
            i = bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)

        # cards

        # if inputs are positive, we can use 0
        # top = [float("inf")] * len(nums)

        # piles = 0
        # for num in nums:
        #     idx = bisect_left(top, num)
        #     if idx == piles:
        #         piles += 1
        #     top[idx] = num
        # return piles
