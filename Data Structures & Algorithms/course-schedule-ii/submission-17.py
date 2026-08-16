class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = {i: 0 for i in range(numCourses)}
        graph = {}
        for u, v in prerequisites:
            indegree[u] += 1
            if v not in graph:
                graph[v] = []
            graph[v].append(u)

        # print(graph, indegree)
        q = deque([])
        for course, prereq in indegree.items():
            # print(course, prereq)
            if prereq == 0:
                q.append(course)
        
        ans = []
        # print(q)
        while q:
            course = q.popleft()
            ans.append(course)
            indegree.pop(course)
            if course not in graph:
                continue
            for dependent in graph[course]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    q.append(dependent)
        return ans if not indegree else []



        indegree = {i: 0 for i in range(numCourses)}
        graph = {}

        for course, prereq in prerequisites:
            indegree[course] += 1
            if prereq not in graph:
                graph[prereq] = []
            graph[prereq].append(course)
        
        q = deque([])
        for node in indegree:
            print(node,'yes')
            if indegree[node] == 0:
                q.append(node)

        ans = []
        print('b4', q)
        while q:
            node = q.popleft()
            ans.append(node)
            if not node in graph: continue
            for course in graph[node]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        return ans if len(ans) == numCourses else []