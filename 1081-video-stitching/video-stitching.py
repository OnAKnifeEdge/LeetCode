class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        if not clips:
            return 0
        clips.sort(key=lambda x: (x[0], -x[1]))
        current_end, farthest_end = 0, 0
        count = 0

        for start, end in clips:
            if start > time:
                continue

            if start > current_end and start > farthest_end:
                return -1

            if start > current_end:
                current_end = farthest_end
                count += 1

                if current_end >= time:
                    return count

            if start <= current_end:
                farthest_end = max(farthest_end, end)

        if current_end < time:
            if farthest_end < time:
                return -1
            count += 1
        return count
