class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        items = list(counter.items())  # List of (num, freq) pairs

        def quick_select(arr, k):
            if not arr:
                return []

            pivot = random.choice(arr)[1]  # Choose frequency as pivot

            left, mid, right = [], [], []
            for num, freq in arr:
                if freq > pivot:  # Compare based on frequency
                    left.append((num, freq))
                elif freq < pivot:
                    right.append((num, freq))
                else:
                    mid.append((num, freq))

            if k <= len(left):
                return quick_select(left, k)
            elif len(left) + len(mid) < k:
                return left + mid + quick_select(right, k - len(left) - len(mid))
            else:
                return left + mid[: k - len(left)]

        result = quick_select(items, k)
        return [num for num, _ in result]
