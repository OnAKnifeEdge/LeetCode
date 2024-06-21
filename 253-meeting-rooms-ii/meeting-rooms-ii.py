class Solution:

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        min_heap = []
        for start, end in intervals:
            if min_heap and start >= min_heap[0]:
                heapreplace(min_heap, end)
            else:
                heappush(min_heap, end)
        return len(min_heap)



    def minMeetingRooms_sort(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        start, end = [], []
        for s, e in intervals:
            start.append(s)
            end.append(e)
        start.sort()
        end.sort()
        result = 0
        count = 0
        i = 0
        j = 0
        while i < n and j < n:
            if start[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            result = max(result, count)
        return result
