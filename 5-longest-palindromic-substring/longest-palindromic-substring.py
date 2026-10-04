class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        # Helper function to expand outward from a given center
        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Length of the palindrome is (right - 1) - (left + 1) + 1 = right - left - 1
            return right - left - 1

        for i in range(len(s)):
            # Check for odd-length palindromes (center is at i)
            len1 = expand_around_center(i, i)
            
            # Check for even-length palindromes (center is between i and i+1)
            len2 = expand_around_center(i, i + 1)
            
            # Get the maximum length found for the current center
            max_len = max(len1, len2)

            # If a longer palindrome is found, update the start and end indices
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]