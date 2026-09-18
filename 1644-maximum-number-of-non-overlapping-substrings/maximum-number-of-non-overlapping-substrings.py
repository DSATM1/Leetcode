class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Find the first and last occurrence of each character
        first = {c: s.find(c) for c in set(s)}
        last = {c: s.rfind(c) for c in set(s)}
        
        valid_intervals = []
        
        # Step 2: Find all valid intervals
        for c in set(s):
            start = first[c]
            end = last[c]
            
            # Try to validate and expand the interval for the current character
            curr = start
            is_valid = True
            
            while curr <= end:
                char_curr = s[curr]
                # If a nested character starts before our current interval's start, 
                # this interval is invalid (we will handle it when we process that earlier character)
                if first[char_curr] < start:
                    is_valid = False
                    break
                
                # Expand the end boundary if the nested character ends later
                end = max(end, last[char_curr])
                curr += 1
                
            if is_valid:
                valid_intervals.append((start, end))
                
        # Step 3: Greedily select the maximum number of non-overlapping intervals
        # Sort by end time to finish intervals as early as possible (minimizes length & maximizes count)
        valid_intervals.sort(key=lambda x: x[1])
        
        res = []
        last_end = -1
        
        for start, end in valid_intervals:
            # If the interval doesn't overlap with the previously added one
            if start > last_end:
                res.append(s[start:end+1])
                last_end = end
                
        return res