class Solution:
    def mostProfitablePath(self, edges, bob, amount):
        n = len(amount)
        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Pre-compute Bob's path times
        bob_time = {}
        def trace_bob(node, parent):
            bob_time[node] = len(bob_time)
            if node == 0:
                return True
            for nei in tree[node]:
                if nei != parent and trace_bob(nei, node):
                    return True
            del bob_time[node]  # Backtrack if not on path to 0
            return False
        
        trace_bob(bob, -1)
        
        def dfs(node, parent, time):
            income = amount[node]
            if node in bob_time:
                if bob_time[node] == time:
                    income //= 2
                elif bob_time[node] < time:
                    income = 0
            
            if len(tree[node]) == 1 and parent != -1:
                return income
                
            max_child = float('-inf')
            for nei in tree[node]:
                if nei != parent:
                    max_child = max(max_child, dfs(nei, node, time + 1))
            
            return income + max_child if max_child != float('-inf') else income
        
        return dfs(0, -1, 0)
