class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ans = []
        visit = set()
        if len(edges)!=n-1: return False

        graph = [[] for _ in range(n)]
        for course, pre in edges:
            graph[course].append(pre)
            graph[pre].append(course)
        
        print(graph)
        def solve(course, prev):
            nonlocal ans
            print(course, prev)
            if course in visit:
                print('course', course, 'in visited')
                return False
            
            visit.add(course)
            for pre in graph[course]:
                if pre == prev: continue
                if not solve(pre, course):
                    print('false for', pre, course)
                    return False

            visit.remove(course)
            return True

        # print(graph)
        for i in range(n):
            if not solve(i, i):
                return False

        return True
        