class Solution:

    def stoneGameIX(self, stones: list[int]) -> bool:
        cnt = [0] * 3
        for x in stones:
            cnt[x % 3] += 1

        if cnt[0] % 2 == 0:
            # When count of 0-remainder stones is even, 0s don't change turn parity.
            # Alice needs at least one 1-remainder or 2-remainder stone to start.
            return cnt[1] > 0 and cnt[2] > 0
        else:
            # When count of 0-remainder stones is odd, 0s flip turn parity once.
            # Alice wins if difference between counts of 1s and 2s is >= 3.
            return abs(cnt[1] - cnt[2]) >= 3