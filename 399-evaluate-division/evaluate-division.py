from collections import defaultdict, deque


class Solution(object):

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # Build the directed graph
        graph = defaultdict(dict)
        for (A, B), val in zip(equations, values):
            graph[A][B] = val
            graph[B][A] = 1.0 / val

        def bfs(start, target):
            if start not in graph or target not in graph:
                return -1.0
            if start == target:
                return 1.0

            queue = deque([(start, 1.0)])
            visited = {start}

            while queue:
                curr_node, curr_prod = queue.popleft()

                if curr_node == target:
                    return curr_prod

                for neighbor, weight in graph[curr_node].items():
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, curr_prod * weight))

            return -1.0

        # Process each query using BFS
        return [bfs(C, D) for C, D in queries]