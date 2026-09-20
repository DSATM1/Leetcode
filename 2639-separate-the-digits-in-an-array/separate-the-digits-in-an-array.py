class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        # List comprehension to iterate through numbers and their digits
        return [int(digit) for num in nums for digit in str(num)]