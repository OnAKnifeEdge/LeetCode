class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # https://leetcode.com/problems/invalid-transactions/solutions/2827880/python3-linear-time-solution-o-n/
        d = defaultdict(lambda: defaultdict(set))  # {name: {time: set()}}
        invalid = set()

        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")
            time = int(time)
            amount = int(amount)
            d[name][time].add(city)

        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")
            time = int(time)
            amount = int(amount)

            if amount > 1000:
                invalid.add(i)
                continue

            for t in range(time - 60, time + 61):
                if t not in d[name]:
                    continue
                if city not in d[name][t] or len(d[name][t]) > 1:
                    invalid.add(i)
        return [t for i, t in enumerate(transactions) if i in invalid]
