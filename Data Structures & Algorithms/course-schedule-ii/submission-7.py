class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            graph[course].append(pre)
        
        visited = set()
        ans = []

        def dfs(idx):
            if len(graph[idx]) == 0:
                ans.append(idx)
            
            if idx in visited:
                return []
            
            visited.add(idx)
            for pre_req in graph[idx]:
                if not dfs(pre_req): return []
            
            visited.remove(idx)
            graph[idx] = []
            ans.append(idx)
            return True
        for i in range(len(graph)):
            if not dfs(i): return []
        return ans