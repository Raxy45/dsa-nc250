class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ans = []
        visit = set()
        if len(edges)!=n-1: return False

        graph = [[] for _ in range(n)]
        for course, pre in edges:
            graph[course].append(pre)
            graph[pre].append(course)
        
        def solve(course, prev):
            if course in visit:
                return False
            
            visit.add(course)
            for pre in graph[course]:
                if pre == prev: continue
                if not solve(pre, course):
                    return False

            return True

        # print(graph)
        for i in range(n):
            if i not in visit and not solve(i, i):
                return False

        return len(visit) == n
        