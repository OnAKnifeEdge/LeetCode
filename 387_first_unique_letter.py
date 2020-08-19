class Solution:
    def first_uniq_char(self, s: str) -> int:
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1

        for index, char in enumerate(s):
            if count[char] == 1:
                return index

        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.first_uniq_char('leetcode'))
