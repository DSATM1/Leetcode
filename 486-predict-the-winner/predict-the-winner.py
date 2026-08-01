class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = nums.copy()

        for i in range(n - 1, -1, -1):
            for j in range(i+1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

        return dp[n - 1] >= 0