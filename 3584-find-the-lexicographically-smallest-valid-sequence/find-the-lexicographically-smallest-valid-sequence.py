class Solution:
    def validSequence(self, word1: str, word2: str):
        n = len(word1)
        m = len(word2)

        if m > n:
            return []

        # suf[i] = maximum number of characters of word2
        # that can be matched using word1[i:]
        suf = [0] * (n + 1)

        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                suf[i] = suf[i + 1] + 1
                j -= 1
            else:
                suf[i] = suf[i + 1]

        ans = []
        j = 0
        used_mismatch = False

        for i in range(n):
            if j == m:
                break

            # Exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use the one allowed mismatch
            elif not used_mismatch:
                remaining = m - j - 1

                # Can remaining word2 be matched after i?
                if suf[i + 1] >= remaining:
                    ans.append(i)
                    j += 1
                    used_mismatch = True

        if j == m:
            return ans

        return []