class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        # Build adjacency list: (neighbor, cost)
        # cost = 1 if edge points away from 0, 0 if edge points towards 0
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append((v, 1))  # u -> v (original direction, needs flip if going from u to v)
            adj[v].append((u, 0))  # v -> u (reverse direction, already correct)

        changes = 0
        visited = set([0])
        stack = [0]

        # Iterative DFS traversal from city 0
        while stack:
            node = stack.pop()
            for neighbor, cost in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    changes += cost
                    stack.append(neighbor)

        return changes