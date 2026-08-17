class Solution(object):
    def maxBuilding(self, n, rest):

        rest.append([1,0])
        rest.sort(key=lambda x: x[0])
        if rest[-1][0] != n:
            rest.append([n, 10**9])

        m = len(rest)

        for i in range(1,m):
            prev_id, prev_h = rest[i-1]
            curr_id, curr_h = rest[i]
            rest[i][1] = min(curr_h,prev_h+(curr_id - prev_id))

        for i in range(m-2, -1, -1):
            next_id, next_h = rest[i+1]
            curr_id, curr_h = rest[i]
            rest[i][1] = min(curr_h, next_h + (next_id - curr_id))

        max_height = 0 
        for i in range(m -1):
            id1, h1 = rest[i]
            id2, h2 = rest[i+1]

            peak = (h1 + h2 +id2 - id1)//2
            max_height = max(max_height, peak)

        return max_height























































        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        