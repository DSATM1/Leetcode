from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        # Check if a palindromic permutation can exist
        odd_chars = [c for c, count in counts.items() if count % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        half_counts = {c: count // 2 for c, count in counts.items()}
        half_len = n // 2
        
        def make_palindrome(first_half: str) -> str:
            if n % 2 == 1:
                return first_half + mid_char + first_half[::-1]
            else:
                return first_half + first_half[::-1]

        candidates = []

        # 1. Exact match for the first half prefix
        temp_counts = half_counts.copy()
        exact_possible = True
        for i in range(half_len):
            c = target[i]
            if temp_counts.get(c, 0) > 0:
                temp_counts[c] -= 1
            else:
                exact_possible = False
                break
        
        if exact_possible:
            cand = make_palindrome(target[:half_len])
            if cand > target:
                candidates.append(cand)

        # 2. Match target[:p] and strictly increase at position p
        for p in range(half_len):
            temp_counts = half_counts.copy()
            possible = True
            for i in range(p):
                c = target[i]
                if temp_counts.get(c, 0) > 0:
                    temp_counts[c] -= 1
                else:
                    possible = False
                    break
            
            if not possible:
                continue
            
            # Try placing characters strictly greater than target[p] at index p
            for ch_code in range(ord(target[p]) + 1, 123):
                ch = chr(ch_code)
                if temp_counts.get(ch, 0) > 0:
                    rem_counts = temp_counts.copy()
                    rem_counts[ch] -= 1
                    
                    suffix_chars = []
                    for c in sorted(rem_counts.keys()):
                        suffix_chars.append(c * rem_counts[c])
                    
                    first_half = target[:p] + ch + "".join(suffix_chars)
                    cand = make_palindrome(first_half)
                    if cand > target:
                        candidates.append(cand)

        return min(candidates) if candidates else ""