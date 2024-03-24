class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        dp = [Counter(target)]
        visited = set(frozenset(Counter(target).items()))
        stickers = [Counter(sticker) for sticker in stickers]

        for result in range(len(target)):
            next_dp = []
            for counter in dp:
                for sticker in stickers:
                    next_counter = counter - sticker
                    if not next_counter:
                        return result + 1
                    visited_check = frozenset(next_counter.items())
                    if visited_check in visited:
                        continue
                    visited.add(visited_check)
                    next_dp.append(next_counter)
            dp = next_dp
        return -1