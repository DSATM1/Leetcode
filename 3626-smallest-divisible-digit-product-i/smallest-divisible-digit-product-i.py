class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def get_digit_product(num: int) -> int:
            product = 1
            while num > 0:
                product *= num % 10
                num //= 10
            return product

        curr = n
        while True:
            if get_digit_product(curr) % t == 0:
                return curr
            curr += 1