class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Initialize graph as an adjacency list
        graph = [[] for _ in range(numCourses)]

        # Build the graph: edge from b to a means "take b before a"
        for a, b in prerequisites:
            graph[b].append(a)

        # visited[i] = 0 → unvisited
        # visited[i] = 1 → visiting (on the current DFS path)
        # visited[i] = 2 → visited and completed
        visited = [0] * numCourses

        def dfs(course):
            # If the course is being visited → we found a cycle
            if visited[course] == 1:
                return False

            # If already completed → no need to recheck
            if visited[course] == 2:
                return True

            # Mark as visiting (entering DFS)
            visited[course] = 1

            # Visit all dependent courses (neighbors)
            for nei in graph[course]:
                if not dfs(nei):
                    return False  # If any neighbor fails, we fail

            # Mark as visited (DFS for this course finished)
            visited[course] = 2
            return True

        # Try to start DFS from every course
        for i in range(numCourses):
            if not dfs(i):
                return False  # If any course has a cycle, return False

        return True  # All courses can be completed (no cycles)
