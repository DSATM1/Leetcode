class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1') < k:
            return ""

        ans = ""
        min_len = float('inf')
        left = 0
        ones_count = 0

        for right in range(len(s)):
            if s[right] == '1':
                ones_count += 1
            
            # Shrink the window when we have exactly k 1's
            while ones_count == k:
                # Move left pointer up to the first '1' in the window
                while s[left] == '0':
                    left += 1
                
                window_len = right - left + 1
                curr_sub = s[left:right + 1]

                if window_len < min_len:
                    min_len = window_len
                    ans = curr_sub
                elif window_len == min_len:
                    ans = min(ans, curr_sub)

                # Move left past the current '1' to search for the next valid substring
                ones_count -= 1
                left += 1

        return ans