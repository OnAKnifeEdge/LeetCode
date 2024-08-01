class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ages = [int(d[-4:-2]) for d in details]
        seniors = [a for a in ages if a > 60]
        return len(seniors)
