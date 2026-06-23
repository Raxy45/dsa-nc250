class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def solve(course):
            if len(graph[course]) == 0:
                return True
            
            if course in visit:
                return False 

            
            visit.add(course)
            for pre_req in graph[course]:
                if not solve(pre_req):
                    return False
            
            visit.remove(course)
            graph[course] = []
            return True

        graph = [[] for _ in range(numCourses)] 

        for course, pre in prerequisites:
            graph[course].append(pre)
        
        visit = set()
        for i in range(len(graph)):
            if not solve(i):
                return False

        return True