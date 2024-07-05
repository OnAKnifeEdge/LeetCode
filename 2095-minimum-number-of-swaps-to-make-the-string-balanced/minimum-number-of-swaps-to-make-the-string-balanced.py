class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0
        for i in s:
            if i == "[":
                count += 1  # increment only if we encounter an open bracket. 
            else:
                if count > 0:  #decrement only if count is positive. Else do nothing and move on. This is because for the case " ] [ [ ] " we do not need to in
                    count -= 1
        return (count + 1) // 2
       