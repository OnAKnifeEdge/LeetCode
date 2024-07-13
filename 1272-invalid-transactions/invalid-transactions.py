class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = set()
        d = defaultdict(list)

        # First pass: populate the dictionary and check for amount > 1000
        for i, trans in enumerate(transactions):
            name, time, amount, city = trans.split(",")
            time, amount = int(time), int(amount)

            if amount > 1000:
                invalid.add(i)

            d[name].append((time, city, i))

        # Second pass: check for transactions within 60 minutes in different cities
        for name, trans_list in d.items():
            for i, (time1, city1, index1) in enumerate(trans_list):
                for time2, city2, index2 in trans_list[i+1:]:
                    if abs(time1 - time2) <= 60 and city1 != city2:
                        invalid.add(index1)
                        invalid.add(index2)

        return [transactions[i] for i in invalid]
