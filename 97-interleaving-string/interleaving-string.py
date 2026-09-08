class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l:
            return False
            
        # Ensure s2 is the smaller string to optimize space for O(min(len(s1), len(s2)))
        if r < c:
            s1, s2, r, c = s2, s1, c, r
            
        dp = [False] * (c + 1)
        dp[0] = True
        
        for j in range(1, c + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
            
        for i in range(1, r + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, c + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or \
                        (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
                        
        return dp[c]