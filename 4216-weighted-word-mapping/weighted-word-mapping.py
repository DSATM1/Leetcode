class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        for word in words:
            total_weight = sum(weights[ord(c) - ord('a')] for c in word)
            remainder = total_weight % 26
            mapped_char = chr(ord('z') - remainder)
            res.append(mapped_char)
        return "".join(res)