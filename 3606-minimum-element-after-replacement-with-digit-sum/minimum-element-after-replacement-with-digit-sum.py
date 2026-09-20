class Solution:
    def minElement(self, nums: list[int]) -> int:
        def get_digit_sum(n: int) -> int:
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total
            
        return min(get_digit_sum(num) for num in nums)