class Pair:
    def __init__(self, frequency, word):
        self.frequency = frequency
        self.word = word

    def __lt__(self, other):
        if self.frequency < other.frequency:
            return True
        # Pair(1, 'b') is lt than Pair(1, 'a') where 'b' > 'a'
        if self.frequency == other.frequency:
            return self.word > other.word


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Option 1
        # max heap 全部， pop 出来的 k 个最大的就是结果
        #  heapify frequency and word, then pop the largest frequency (*-1 max heap)
        # O(n + klogk) 不好 not flexible,
        # when 'k' is a considerable fraction of 'N' or close to 'N', 'k log N' is less than 'N log k'.

        # Option 2
        #  min_heap: 只维护一个 k 大的 heap，小的都被 pop 掉了
        # O(n*logk) 很 flexible 而且 k 小的时候 performance 好
        # O(N)+O(Nlogk)+O(klogk)=O(Nlogk)
        counter = Counter(words)
        min_heap = []
        for word, frequency in counter.items():
            heappush(min_heap, Pair(frequency, word))
            if len(min_heap) > k:
                heappop(min_heap)
        # now min_heap has the top k words
        return [p.word for p in sorted(min_heap, reverse=True)]
