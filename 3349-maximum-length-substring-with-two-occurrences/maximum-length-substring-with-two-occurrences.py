class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counts = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # Expand the window by including s[right]
            counts[s[right]] = counts.get(s[right], 0) + 1
            
            # Shrink the window from the left if any character count exceeds 2
            while counts[s[right]] > 2:
                counts[s[left]] -= 1
                left += 1
            
            # Update the maximum valid window size
            max_len = max(max_len, right - left + 1)
            
        return max_len