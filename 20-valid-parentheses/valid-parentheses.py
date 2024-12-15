class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        parentheses = {"]": "[", ")": "(", "}": "{"}
        stk = []
        for c in s:
            if c in parentheses.values():
                stk.append(c)
            elif c in parentheses.keys():
                if not stk:
                    return False
                if stk.pop() != parentheses[c]:
                    return False
            else:
                return False

        return not bool(stk)
