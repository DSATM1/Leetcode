from math import lcm
from itertools import combinations
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Step 1: Remove redundant coins (multiples of smaller coins)
        coins.sort()
        filtered_coins = []
        for c in coins:
            if not any(c % existing == 0 for existing in filtered_coins):
                filtered_coins.append(c)
        
        # Step 2: Precompute LCMs and signs for all subset combinations
        subsets = []
        n = len(filtered_coins)
        for r in range(1, n + 1):
            sign = 1 if r % 2 == 1 else -1
            for comb in combinations(filtered_coins, r):
                curr_lcm = comb[0]
                for coin in comb[1:]:
                    curr_lcm = lcm(curr_lcm, coin)
                subsets.append((curr_lcm, sign))

        # Helper to count unique amounts <= m
        def count_amounts(m: int) -> int:
            return sum(sign * (m // l) for l, sign in subsets)

        # Step 3: Binary search for the kth smallest amount
        left = min(filtered_coins)
        right = min(filtered_coins) * k
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if count_amounts(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans