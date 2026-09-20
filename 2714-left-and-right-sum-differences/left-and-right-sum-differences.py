class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        left_sum = 0
        right_sum = sum(nums)
        ans = []
        
        for num in nums:
            # The current number is neither in the left sum nor the right sum for this index
            right_sum -= num
            
            # Calculate the absolute difference
            ans.append(abs(left_sum - right_sum))
            
            # Add the current number to the left sum for the next index
            left_sum += num
            
        return ans