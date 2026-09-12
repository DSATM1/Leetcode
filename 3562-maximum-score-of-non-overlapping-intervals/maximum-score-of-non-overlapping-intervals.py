import bisect

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        
        # Store intervals with their original indices and sort them by end time.
        # Format: (start, end, weight, original_index)
        arr = []
        for idx, (s, e, w) in enumerate(intervals):
            arr.append((s, e, w, idx))
            
        arr.sort(key=lambda x: x[1]) 
        
        # dp[i][c] stores a tuple: (-total_weight, lexicographically_smallest_indices)
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        # Extract just the end times to make binary searching easier
        end_times = [x[1] for x in arr]
        
        for i in range(1, n + 1):
            start, end, weight, orig_idx = arr[i - 1]
            
            # bisect_left finds the first index where end >= start. 
            valid_idx = bisect.bisect_left(end_times, start, 0, i - 1)
            
            for count in range(1, 5):
                # Option 1: Do not include the current interval
                skip = dp[i - 1][count]
                
                # Option 2: Include the current interval
                prev_weight, prev_indices = dp[valid_idx][count - 1]
                take_weight = prev_weight - weight 
                take_indices = sorted(prev_indices + [orig_idx])
                take = (take_weight, take_indices)
                
                # Record the optimal choice for this state
                dp[i][count] = min(skip, take)
                
        # The result for considering all n intervals and picking up to 4 of them
        return dp[n][4][1]