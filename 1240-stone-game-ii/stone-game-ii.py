class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # Precompute suffix sums
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        memo = {}

        def dp(i: int, m: int) -> int:
            # Base Case: Player can take all remaining piles
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            if (i, m) in memo:
                return memo[(i, m)]
            
            max_stones = 0
            # Try taking X piles where 1 <= X <= 2 * M
            for x in range(1, 2 * m + 1):
                # Current player score = Total remaining - Opponent's optimal score next turn
                stones_taken = suffix_sum[i] - dp(i + x, max(m, x))
                max_stones = max(max_stones, stones_taken)
            
            memo[(i, m)] = max_stones
            return max_stones

        return dp(0, 1)