class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        # If k is 1, every single character is a valid palindrome
        if k == 1:
            return n
        
        res = 0
        i = 0
        
        # Helper function to check if s[l:r+1] is a palindrome
        def check(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
            
        while i <= n - k:
            # Check if there is a palindrome of length k
            if check(i, i + k - 1):
                res += 1
                i += k  # Jump past this palindrome
            # Check if there is a palindrome of length k + 1
            elif i < n - k and check(i, i + k):
                res += 1
                i += k + 1 # Jump past this palindrome
            else:
                i += 1
                
        return res