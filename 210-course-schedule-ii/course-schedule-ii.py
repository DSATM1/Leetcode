from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Create an adjacency list to represent the graph
        adj = [[] for _ in range(numCourses)]
        # Array to track the number of prerequisites for each course
        indegree = [0] * numCourses
        
        # Populate the adjacency list and in-degree array
        for dest, src in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1
            
        # Initialize a queue with all courses that have no prerequisites
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                
        ans = []
        
        # Process the courses
        while q:
            node = q.popleft()
            ans.append(node)
            
            # Decrease the in-degree of neighboring courses
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                # If a course now has no prerequisites, add it to the queue
                if indegree[neighbor] == 0:
                    q.append(neighbor)
                    
        # If the number of courses in our answer equals numCourses, 
        # we successfully found a topological order.
        if len(ans) == numCourses:
            return ans
        
        # Otherwise, there was a cycle, and it's impossible to finish all courses.
        return []