class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        processes = defaultdict(list)  # {parent_pid: [pid]}

        # Build the graph.
        for child, parent in zip(pid, ppid):
            processes[parent].append(child)

        to_be_killed = []
        q = deque([kill])

        while q:
            current_process = q.popleft()
            to_be_killed.append(current_process)
            q.extend(processes[current_process])

        return to_be_killed
