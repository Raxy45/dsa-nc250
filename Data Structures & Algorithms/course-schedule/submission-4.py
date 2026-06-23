class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            graph[course].append(pre)
        
        visited = set()

        def dfs(idx):
            print('dfs for', idx, visited)
            if len(graph[idx]) == 0:
                print('NO PRE_REQ')
                return True
            
            if idx in visited:
                return False
            
            visited.add(idx)
            for pre_req in graph[idx]:
                if not dfs(pre_req): return False
            
            visited.remove(idx)
            graph[idx] = []
            return True

        print(graph)
        for i in range(len(graph)):
            if not dfs(i): return False
        return True