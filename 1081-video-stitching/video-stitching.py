class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # If the time range to cover is zero, no clips are needed.
        if time == 0:
            return 0

        if not clips:
            return -1

        clips.sort(key=lambda x: (x[0], -x[1]))
        current_end, farthest_end = 0, 0
        count = 0

        for start, end in clips:

            if start > time:
                continue

            if start <= current_end:
                farthest_end = max(farthest_end, end)

            elif start <= farthest_end:
                current_end = farthest_end
                count += 1
                farthest_end = max(farthest_end, end)
            else:
                return -1  # A gap is found

            if current_end >= time:
                return count

            if farthest_end >= time:
                return count + 1

        return -1
