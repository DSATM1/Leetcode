class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals based on their end time
        intervals.sort(key=lambda x: x[1])
        
        removals = 0
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            # If current interval starts before the previous end, there is an overlap
            if intervals[i][0] < prev_end:
                removals += 1
            else:
                # Update end time to current interval's end time
                prev_end = intervals[i][1]
                
        return removals