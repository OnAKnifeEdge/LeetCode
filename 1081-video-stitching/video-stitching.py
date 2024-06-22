class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # If the target time is 0 or less, no clips are needed.
        if time <= 0:
            return 0

        # Sort clips based on their start times; for ties, longer clips come first.
        clips.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        current_end, next_end = 0, 0
        for start, end in clips:
            # Skip any clips that start after the current target time; they are not needed.
            if start > time:
                break

            if start > current_end and start > next_end:
                # Start is beyond both current and next potential end, impossible to continue
                return -1
            elif start > current_end:
                # We need to make a jump here
                current_end = next_end
                count += 1
                if current_end >= time:
                    # If we already cover the required time interval, break early
                    break

            if start <= current_end:
                # Extend the furthest reach within the current segment
                next_end = max(next_end, end)

        # Final check after processing all clips
        if current_end < time:
            if next_end < time:
                return -1
            count += 1
        return count
