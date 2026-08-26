class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def backtrack(index: int, current_comb: list):
            if index == len(digits):
                res.append("".join(current_comb))
                return

            for char in digit_to_char[digits[index]]:
                current_comb.append(char)
                backtrack(index + 1, current_comb)
                current_comb.pop()

        backtrack(0, [])
        return res