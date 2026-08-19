class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        total = 0
        curr_num = 0
        sign = 1  # 1 for '+', -1 for '-'

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char in ('+', '-'):
                total += sign * curr_num
                curr_num = 0
                sign = 1 if char == '+' else -1
            elif char == '(':
                # Push the running total and sign onto stack for later
                stack.append(total)
                stack.append(sign)
                # Reset total and sign for the inner expression
                total = 0
                sign = 1
            elif char == ')':
                total += sign * curr_num
                curr_num = 0
                # Apply previous sign before '('
                total *= stack.pop()
                # Add total before '('
                total += stack.pop()

        # Add any remaining calculated number
        return total + (sign * curr_num)