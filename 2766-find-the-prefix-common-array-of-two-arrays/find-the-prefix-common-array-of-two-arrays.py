class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s1, s2 = set(), set()
        prefix = []
        for a, b in zip(A, B):
            s1.add(a)
            s2.add(b)
            count = len(s1 & s2)
            prefix.append(count)
        return prefix
