from sortedcontainers import SortedList

class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (4 * size)

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, start, end, l, r):
        if r < start or end < l or l > r:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self.query(2 * node, start, mid, l, r)
        p2 = self.query(2 * node + 1, mid + 1, end, l, r)
        return max(p1, p2)


class Solution:
    def getResults(self, queries: list[list[int]]) -> list[bool]:
        # Maximum possible coordinate for obstacles
        MAX_X = min(50000, 3 * len(queries)) + 1
        
        st = SegmentTree(MAX_X)
        obstacles = SortedList([0, MAX_X])
        
        # Initialize segment tree with boundary obstacle at MAX_X
        st.update(1, 0, MAX_X - 1, MAX_X, MAX_X)

        ans = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = obstacles.bisect_right(x)
                prev_obs = obstacles[idx - 1]
                next_obs = obstacles[idx]
                
                # Insert x and update gap values in segment tree
                obstacles.add(x)
                st.update(1, 0, MAX_X - 1, x, x - prev_obs)
                if next_obs < MAX_X:
                    st.update(1, 0, MAX_X - 1, next_obs, next_obs - x)

            elif q[0] == 2:
                x, sz = q[1], q[2]
                idx = obstacles.bisect_right(x)
                prev_obs = obstacles[idx - 1]
                
                # Max gap in range [0, prev_obs] or the final partial range [prev_obs, x]
                max_gap = max(st.query(1, 0, MAX_X - 1, 0, prev_obs), x - prev_obs)
                ans.append(max_gap >= sz)

        return ans