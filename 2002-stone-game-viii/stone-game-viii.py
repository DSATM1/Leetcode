class Solution:

    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)

        # Compute prefix sums array
        pref = stones[:]
        for i in range(1, n):
            pref[i] += pref[i - 1]

        # DP state: max difference score the current player can achieve
        # starting at choice index >= i.
        # Base case: if taking all stones up to index n-1, gain is pref[n-1].
        ans = pref[-1]

        # Iterate backward from index n - 2 down to 1 (x must be > 1, so index >= 1)
        for i in range(n - 2, 0, -1):
            ans = max(ans, pref[i] - ans)

        return ans