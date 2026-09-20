class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Convert string to a set for O(1) lookups
        word_set = set(word)
        count = 0
        
        # Check every lowercase letter in the alphabet
        for char in "abcdefghijklmnopqrstuvwxyz":
            if char in word_set and char.upper() in word_set:
                count += 1
                
        return count