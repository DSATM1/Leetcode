class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # If the right neighbor is greater, a peak must exist on the right side
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            # Otherwise, a peak exists on the left side (including mid)
            else:
                right = mid

        return left