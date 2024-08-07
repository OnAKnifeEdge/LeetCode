class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)

        def trim():
            # Remove leading spaces
            while s and s[0] == " ":
                s.pop(0)

            # Remove trailing spaces
            while s and s[-1] == " ":
                s.pop()

            # Merge multiple spaces into one
            write = 1
            for read in range(1, len(s)):
                current_char = s[read]
                prev_char = s[write - 1]

                if current_char != " " or prev_char != " ":
                    s[write] = current_char
                    write += 1

            # Remove extra spaces
            while len(s) > write:
                s.pop()

        def reverse():
            i, j = 0, len(s) - 1
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        def reverse_each_word():
            start = 0
            for end in range(len(s) + 1):
                if end == len(s) or s[end] == " ":
                    i, j = start, end - 1
                    while i < j:
                        s[i], s[j] = s[j], s[i]
                        i += 1
                        j -= 1
                    start = end + 1


        trim()
        reverse()
        reverse_each_word()
        return "".join(s)
