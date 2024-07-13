class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = set()
        d = defaultdict(list)

        # First pass: populate the dictionary and check for amount > 1000
        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")
            time, amount = int(time), int(amount)

            if amount > 1000:
                invalid.add(i)

            d[name].append((time, city, i))

        # Second pass: check for transactions within 60 minutes in different cities
        for name, record in d.items():
            record.sort()
            for i, (time, city, index) in enumerate(record):
                # Find the range of transactions within 60 minutes
                start = bisect.bisect_left(record, (time - 60, "", 0))
                end = bisect.bisect_right(record, (time + 60, "", float("inf")))

                # Check transactions within this range
                for j in range(start, end):
                    if i != j and record[j][1] != city:
                        invalid.add(index)
                        invalid.add(record[j][2])

        return [transactions[i] for i in invalid]
