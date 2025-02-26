class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        no_deletion = arr[0]
        one_deletion = 0
        max_sum = arr[0]

        for num in arr[1:]:
            one_deletion = max(no_deletion, one_deletion + num)
            no_deletion = max(no_deletion + num, num)
            max_sum = max(max_sum, no_deletion, one_deletion)
        return max_sum
