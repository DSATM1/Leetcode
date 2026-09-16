import math

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # We need to choose 2k points from n + k - 1 points
        ans = math.comb(n + k - 1, 2 * k)
        
        return ans % MOD