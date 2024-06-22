class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        """
        If the start time of a clip is greater than the current time target,
            it's irrelevant, and we continue to the next.

        If the clip starts within the current covered range (i.e., start <= current_end),
            we update farthest_end to include this clip's end if it extends our reach further.

        If the clip starts beyond current_end but within the range that farthest_end can extend to,
            we "jump" to this farthest_end by updating current_end and increment the count.
            Then, we consider the current clip for further extending farthest_end.
            
        If the clip starts beyond both current_end and farthest_end,
            there's a gap that cannot be covered, and hence, we return -1.
        """
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
