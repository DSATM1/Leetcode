class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        dp0 = dp1 = dp2 = 0 

        for i in range(n - 1, -1, -1):
            curr_sum = 0 
            best_diff = float('-inf')

            for k in range(1, 4):
                if i + k - 1 < n:
                    curr_sum += stoneValue[i + k - 1]
                    next_dp = dp0 if k == 1 else (dp1 if k == 2 else dp2)
                    best_diff = max(best_diff, curr_sum - next_dp)

            dp0, dp1, dp2 = best_diff, dp0, dp1

        if dp0 > 0:
            return "Alice"
        elif dp0 < 0:
            return "Bob"
        else:
            return "Tie"