class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count_dict = {}
        count = 0
        for n in nums:
            c = k - n
            if count_dict.get(c, 0) > 0:
                count_dict[c] -= 1
                count += 1
            else:
                count_dict[n] = count_dict.get(n, 0) + 1
        return count
        