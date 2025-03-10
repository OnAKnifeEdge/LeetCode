class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        if not colors:
            return 0
        n = len(colors)
        count = 0
        alternating_cnt = 1
        last_color = colors[0]

        for i in range(1, n + k - 1):
            idx = i % n

            if colors[idx] == last_color:
                alternating_cnt = 1
                last_color = colors[idx]
                continue

            alternating_cnt += 1
            if alternating_cnt >= k:
                count += 1

            last_color = colors[idx]

        return count
