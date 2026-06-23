class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        complete_prereq = [[] for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]

        # construct graph
        for pre_req, course in prerequisites:
            graph[course].append(pre_req)

        def dfs(course):
            if course in visit:
                return complete_prereq[course]
            if graph[course] == []:
                return []

            for pre_req in graph[course]:
                complete_prereq[course].append(pre_req)
                complete_prereq[course].extend(dfs(pre_req))
            
            visit.add(course)
            return complete_prereq[course]

        # contruct complete pre-reqs
        visit = set()
        for i in range(numCourses):
            dfs(i)
        
        for i in range(len(complete_prereq)):
            complete_prereq[i] = set(complete_prereq[i])

        ans = [False] * len(queries)

        # print(f'{graph = }')
        # print(f'{complete_prereq = }')

        # print('queries')
        for i, query in enumerate(queries):
            # print(query[0], query[1])
            # print(complete_prereq[query[1]])
            if query[0] in complete_prereq[query[1]]: ans[i] = True
        return ans