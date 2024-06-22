class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # If the target time is 0 or less, no clips are needed.
        if time <= 0:
            return 0

        # Sort clips based on their start times; for ties, longer clips come first.
        clips.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        current_end, furtherest_end = 0, 0
        for start, end in clips:
            # Skip any clips that start after the target
            if start > time:
                break

            if start > current_end and start > furtherest_end:
                # if gap
                return -1

            # Making a Jump:
            # If a clip starts after the current_end but not beyond the next_end,
            # the coverage is extended to next_end, and count is incremented.
            if start > current_end:
                current_end = furtherest_end
                count += 1
                if current_end >= time:
                    # If we already cover the required time interval
                    return count

            # Extending furtherest_end that can be reached without making another jump
            # for clips that start within the current coverage (start <= current_end)
            if start <= current_end:
                furtherest_end = max(furtherest_end, end)

        if current_end < time:
            if furtherest_end < time:
                return -1
            count += 1
        return count
