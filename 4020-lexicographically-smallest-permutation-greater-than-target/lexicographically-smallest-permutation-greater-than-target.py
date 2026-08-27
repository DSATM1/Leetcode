from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = Counter(s)
        
        # Try matching prefix of length `i` with `target`
        # and making character at `i` strictly greater than `target[i]`
        for i in range(n, -1, -1):
            # Check if we can form the prefix target[:i]
            curr_freq = Counter(s)
            possible = True
            for j in range(i):
                if curr_freq[target[j]] > 0:
                    curr_freq[target[j]] -= 1
                else:
                    possible = False
                    break
            
            if not possible:
                continue
            
            # If matching the full length, it must be strictly greater, not equal
            if i == n:
                continue
                
            # Try to pick a character strictly greater than target[i]
            for c in sorted(curr_freq.keys()):
                if c > target[i] and curr_freq[c] > 0:
                    # Place character `c` at position `i`
                    curr_freq[c] -= 1
                    
                    # Fill the rest of the string greedily in sorted order
                    remaining = []
                    for char in sorted(curr_freq.keys()):
                        remaining.append(char * curr_freq[char])
                    
                    return target[:i] + c + "".join(remaining)
                    
        return ""