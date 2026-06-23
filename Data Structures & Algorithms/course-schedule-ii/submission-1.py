class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = [-1] * numCourses
        print(ans, len(ans))
        visit = set()

        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[course].append(pre)
        

        def solve(course):
            nonlocal ans
            if course in visit:
                return False

            if graph[course] == []:
                print(course, len(ans))
                if ans[course] == -1:
                    ans[course] = course
                return True
            
            visit.add(course)
            for pre in graph[course]:
                if not solve(pre):
                    return False

            visit.remove(course)
            graph[course] = []
            return True

        print(graph)
        for i in range(numCourses):
            if not solve(i):
                return []
        
        for i in range(len(ans)):
            if ans[i] == -1:
                ans[i] = i
        return ans
