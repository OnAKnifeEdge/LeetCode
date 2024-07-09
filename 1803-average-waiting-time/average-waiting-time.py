class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_waiting_time = 0
        chef_free_time = 0

        for arrival, time in customers:
            chef_free_time = max(chef_free_time, arrival)
            waiting_time = chef_free_time - arrival
            total_waiting_time += waiting_time + time
            chef_free_time += time

        return total_waiting_time / len(customers)
