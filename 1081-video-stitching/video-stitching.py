from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # If the time range to cover is zero, no clips are needed.
        if time == 0:
            return 0
        # If there are no clips but the time to cover is greater than 0, it's impossible to cover.
        if not clips:
            return -1

        clips.sort(key=lambda x: (x[0], -x[1]))
        current_end, farthest_end = 0, 0
        count = 0

        for start, end in clips:
            # Clips beyond the target time are irrelevant; we continue the loop.
            if start > time:
                continue

            # If this clip can potentially extend the coverage without a gap.
            if start <= current_end:
                farthest_end = max(farthest_end, end)
            # If we encounter a gap or the start of this clip is beyond the farthest_end we could reach,
            # we make a 'jump' to extend the coverage with previous `farthest_end`.
            elif start <= farthest_end:
                current_end = farthest_end
                count += 1
                farthest_end = max(farthest_end, end)
            else:
                return -1  # A gap is found that we cannot bridge.

            # If at any point we've extended (or are able to extend) the coverage beyond the target time, we increment and return.
            if current_end >= time:
                return count
            # Check this condition again after updating `current_end`.
            if farthest_end >= time:
                return count + 1

        # # Final check - in case the last update to `farthest_end` was able to cover the time but wasn't accounted for in the loop.
        # if farthest_end >= time:
        #     count += 1
        #     return count

        # If, after all, the total covered time doesn't reach the target, return -1.
        return -1
