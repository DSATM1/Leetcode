class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        # dp[i] will store the number of distinct subsequences ending with the i-th lowercase English letter
        dp = [0] * 26
        
        for char in s:
            idx = ord(char) - ord('a')
            # Calculate total distinct subsequences formed so far plus the single character itself
            total = (sum(dp) + 1) % MOD
            dp[idx] = total
            
        return sum(dp) % MOD