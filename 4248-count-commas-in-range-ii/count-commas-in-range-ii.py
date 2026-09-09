class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_commas = 0
        
        # Iterate through digit lengths from 4 up to 16 (since n <= 10^15)
        # Length L covers numbers from 10^(L-1) to min(n, 10^L - 1)
        for L in range(4, 18):
            start = 10 ** (L - 1)
            if start > n:
                break
            end = min(n, 10 ** L - 1)
            count = end - start + 1
            commas_per_num = (L - 1) // 3
            total_commas += count * commas_per_num
            
        return total_commas