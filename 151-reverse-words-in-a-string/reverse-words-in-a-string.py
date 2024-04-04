class Solution:

    def trim(self, s: str) -> str:
        left, right = 0, len(s) - 1
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1

        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1
        return output

    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

    def reverse_each_word(self, l: list) -> None:
        start, end  = 0, 0
        while start < len(l):
            # go to the end of the word
            while end < len(l) and l[end] != ' ':
                end += 1
            # reverse the word
            self.reverse(l, start, end - 1)
            # move to the next word
            start = end + 1
            end += 1
        
    def reverseWords(self, s: str) -> str:
        l = self.trim(s)

        self.reverse(l, 0, len(l) - 1)

        self.reverse_each_word(l)

        return ''.join(l)


        