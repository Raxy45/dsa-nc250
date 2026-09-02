class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ind = [0] * numCourses
        graph = defaultdict(set)

        for u, v in prerequisites:
            graph[v].add(u) # v needs to know who all are dependent on me
            ind[u] += 1
        
        q = deque()
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)
            
        ans = []
        while q:
            node = q.popleft()
            # if graph[node] == 0:
                # graph.
            ans.append(node)
            for nei in graph[node]:
                ind[nei] -= 1
                if ind[nei] == 0:
                    q.append(nei)

        return True if len(ans)==numCourses else False

        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        print(indegree, adj)
        finish = 0
        while q:
            node = q.popleft()
            print('first doing', node)
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return finish == numCourses