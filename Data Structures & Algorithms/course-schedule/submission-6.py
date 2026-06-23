class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        print(indegree, adj)
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return finish == numCourses
        
    def canFinishDFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            graph[course].append(pre)
        
        visited = set()

        def dfs(idx):
            if len(graph[idx]) == 0:
                return True
            
            if idx in visited:
                return False
            
            visited.add(idx)
            for pre_req in graph[idx]:
                if not dfs(pre_req): return False
            
            visited.remove(idx)
            graph[idx] = []
            return True
        for i in range(len(graph)):
            if not dfs(i): return False
        return True