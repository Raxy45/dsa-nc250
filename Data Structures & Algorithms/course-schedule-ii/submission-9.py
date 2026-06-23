class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        ans = []
        visited = set()
        def dfs(curr):
            nonlocal ans, visited
            visited.add(curr)
            for prereq in graph[curr]:
                if prereq in visited:
                    return False
                if not dfs(prereq):
                    return False
            visited.remove(curr)
            graph[curr] = []
            ans.append(curr)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        return ans
                
