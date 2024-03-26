class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        def count(left: int, right: int) -> int:
            cnt = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
            return cnt

        for i in range(len(s)):
            result += count(i, i)
            result += count(i, i + 1)
        return result



            
        