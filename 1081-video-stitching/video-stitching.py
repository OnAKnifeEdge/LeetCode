class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # If the target time is 0 or less, no clips are needed.
        if time <= 0:
            return 0

        # Sort clips based on their start times; for ties, longer clips come first.
        clips.sort(key=lambda x: (x[0], -x[1]))

        ret, cur_end, next_end = 0, 0, 0
        for start, end in clips:
            # Skip any clips that start after the current target time; they are not needed.
            if start > time:
                break

            if start > cur_end and start > next_end:
                # Start is beyond both current and next potential end, impossible to continue
                return -1
            elif start > cur_end:
                # We need to make a jump here
                cur_end, ret = next_end, ret + 1
                if cur_end >= time:
                    # If we already cover the required time interval, break early
                    break

            if start <= cur_end:
                # Extend the furthest reach within the current segment
                next_end = max(next_end, end)

        # Final check after processing all clips
        if cur_end < time:
            if next_end >= time:
                # One last jump needed
                ret += 1
            else:
                # If the next_end does not reach or exceed the time required, it's impossible
                return -1

        return ret
