class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        
        # dp[j] represents the number of distinct subsequences of prefix of s 
        # that equal the prefix of t of length j.
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string t can always be formed once by an empty subsequence of s
        
        for i in range(1, m + 1):
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]