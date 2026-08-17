class Solution:
    def processStr(self, s: str, k: int) -> str:
        lens = []
        curr_len = 0
        
        for ch in s:
            if ch == '*':
                curr_len = max(curr_len - 1, 0)
            elif ch == '#':
                curr_len *= 2
            elif ch != '%':
                curr_len += 1

            lens.append(curr_len)
            
        if k >= curr_len:
            return "."
            
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            
            if ch == '*':

                continue
                
            elif ch == '#':

                half_len = lens[i] // 2
                if k >= half_len:
                    k -= half_len
                    
            elif ch == '%':

                k = lens[i] - 1 - k
                
            else:
                
                if k == lens[i] - 1:
                    return ch
                    
        return "."        