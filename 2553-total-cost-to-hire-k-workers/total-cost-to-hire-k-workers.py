class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        head_workers = costs[:candidates]

        # n = len(costs)
        # if candidates > n // 2:
        #     tail_workers = costs[candidates - n:]
        # else:
        #     tail_workers = costs[-candidates:]

        tail_workers = costs[max(candidates, len(costs) - candidates):]

        heapify(head_workers)
        heapify(tail_workers)
        
        cost = 0
        next_head, next_tail = candidates, len(costs) - 1 - candidates

        for _ in range(k):
            # select from head_workers
            if head_workers and tail_workers and head_workers[0] <= tail_workers[0] or not tail_workers:
                cost += heappop(head_workers)

                if next_head <= next_tail:
                    heappush(head_workers, costs[next_head])
                    next_head += 1
                # if next_head > next_tail:
                #     continue

                # # only refill if there are workers outside the queue
                # heappush(head_workers, costs[next_head])
                # next_head += 1
            # select from tail_workers
            else:
                cost += heappop(tail_workers)

                if next_head <= next_tail:
                    heappush(tail_workers, costs[next_tail])
                    next_tail -= 1


                # if next_tail > next_tail:
                #     continue

                # heappush(tail_workers, costs[next_tail])
                # next_tail -= 1
        return cost


            



        