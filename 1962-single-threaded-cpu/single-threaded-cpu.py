class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        indexed_tasks = [(e, p, i) for i, (e, p) in enumerate(tasks)]

        indexed_tasks.sort(key=lambda x: x[0])

        now, i = 0, 0
        min_heap = []
        result = []  # will be the result

        while len(result) < n:

            # when the task is available, push available tasks to min_heap
            while i < n and indexed_tasks[i][0] <= now:
                _, p, idx = indexed_tasks[i]
                heappush(min_heap, (p, idx))
                i += 1

            if min_heap:
                p, idx = heappop(min_heap)
                now += p
                result.append(idx)

            elif i < n:  # heap is empty but there is still tasks left
                # go to the next task
                now = indexed_tasks[i][0]
        return result
