class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = {i: 0 for i in range(numCourses)}
        graph = {}

        for course, prereq in prerequisites:
            indegree[course] += 1
            if prereq not in graph:
                graph[prereq] = []
            graph[prereq].append(course)
        
        q = deque([])
        for node in indegree:
            if indegree[node] == 0:
                q.append(node)

        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            if not node in graph: continue
            for course in graph[node]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        return ans if len(ans) == numCourses else []