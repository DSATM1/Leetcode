class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        res = []
        left, right = 0, len(products) - 1

        for i, char in enumerate(searchWord):
            # Move left pointer rightward until the product matches the prefix up to character i
            while left <= right and (len(products[left]) <= i or products[left][i] != char):
                left += 1

            # Move right pointer leftward until the product matches the prefix up to character i
            while left <= right and (len(products[right]) <= i or products[right][i] != char):
                right -= 1

            # Collect up to 3 products from the valid range [left, right]
            suggestions = []
            for j in range(left, min(left + 3, right + 1)):
                suggestions.append(products[j])

            res.append(suggestions)

        return res