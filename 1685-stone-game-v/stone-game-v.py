class Solution:
    def stoneGameV(self, A):
        n = len(A)

        # dp[i][j] = maximum score for A[i:j+1]
        dp = [[0] * n for _ in range(n)]

        # mx[i][j] stores:
        # max(dp[i][k] + sum(A[i:k+1])) for k in [i, j]
        #
        # mx[j][i] stores the corresponding right-side values.
        mx = [[0] * n for _ in range(n)]

        # Base case
        for i in range(n):
            mx[i][i] = A[i]

        # Process intervals by right endpoint
        for j in range(1, n):

            mid = j
            sm = A[j]
            right = 0

            for i in range(j - 1, -1, -1):

                sm += A[i]

                # Move mid while the right side is
                # not larger than the left side.
                while (right + A[mid]) * 2 <= sm:
                    right += A[mid]
                    mid -= 1

                # Equal partition
                if right * 2 == sm:
                    dp[i][j] = mx[i][mid]

                # left side is smaller
                if mid != i:
                    dp[i][j] = max(
                        dp[i][j],
                        mx[i][mid - 1]
                    )

                # right side is smaller
                if mid != j:
                    dp[i][j] = max(
                        dp[i][j],
                        mx[j][mid + 1]
                    )

                # Update prefix-side maximum
                mx[i][j] = max(
                    mx[i][j - 1],
                    dp[i][j] + sm
                )

                # Update suffix-side maximum
                mx[j][i] = max(
                    mx[j][i + 1],
                    dp[i][j] + sm
                )

        return dp[0][n - 1]