class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # If the required sum exceeds the maximum possible sum (all 9s), it's impossible
        if sum > num * 9:
            return ""
        
        # Calculate how many 9s we can use and what the remainder digit will be
        q, r = divmod(sum, 9)
        
        # Build the string by string repetition (O(N) time complexity)
        result = "9" * q
        
        # If we haven't filled all 'num' digits, append the remainder and pad with 0s
        if q < num:
            result += str(r)
            result += "0" * (num - q - 1)
            
        return result