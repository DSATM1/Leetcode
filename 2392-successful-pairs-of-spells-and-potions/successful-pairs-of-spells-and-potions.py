class Solution:

    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        m = len(potions)
        pairs = []

        for spell in spells:
            # Minimum potion strength needed: ceil(success / spell)
            target = (success + spell - 1) // spell

            # Find the first potion with strength >= target
            idx = bisect_left(potions, target)

            # All potions from idx to the end are successful
            pairs.append(m - idx)

        return pairs