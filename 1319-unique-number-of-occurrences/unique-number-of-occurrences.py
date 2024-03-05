class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        count_values = counter.values()
        return len(set(count_values)) == len(count_values)
