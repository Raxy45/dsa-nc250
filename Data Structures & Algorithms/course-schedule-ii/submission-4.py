class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        visit, ans_check = set(), set()

        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[course].append(pre)
        

        def solve(course):
            nonlocal ans
            if course in visit:
                return False

            if graph[course] == []:
                if course not in ans_check:
                    ans_check.add(course)
                    ans.append(course)
                return True
            
            visit.add(course)
            for pre in graph[course]:
                if not solve(pre):
                    return False

            visit.remove(course)
            if course not in ans_check:
                ans_check.add(course)
                ans.append(course)
            graph[course] = []
            return True

        print(graph)
        for i in range(numCourses):
            if not solve(i):
                return []

        return ans
