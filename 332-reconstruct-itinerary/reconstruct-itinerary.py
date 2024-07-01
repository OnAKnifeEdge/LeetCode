class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flight_map = defaultdict(list)

        # Build the graph
        for start, end in tickets:
            flight_map[start].append(end)

        # # Sort the destinations to ensure lexical order
        flight_map = {k: sorted(v, reverse=True) for k, v in flight_map.items()}

        itinerary = []

        def dfs(node):
            while node in flight_map and flight_map[node]:
                # Get the lexicographically largest destination to explore first
                next_dest = flight_map[node].pop()
                dfs(next_dest)
            itinerary.append(node)

        dfs("JFK")

        # Reverse the itinerary to get the correct order
        return list(reversed(itinerary))
