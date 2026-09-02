class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]

        # generate graph
        for pre, course in prerequisites:
            graph[course].append(pre)

        def dfs(course):
            if course in complete_prereq:
                # all pre-reqs of current course are already traversed
                return complete_prereq[course]

            for pre_req in graph[course]:
                updated_prereq = dfs(pre_req)
                complete_prereq[course] |= updated_prereq
            
            complete_prereq[course].add(course)
            return complete_prereq[course]
            
        complete_prereq = defaultdict(set)
        for course in range(numCourses):
            dfs(course)
            
        # answering queries
        result = []
        for u, v in queries:
            result.append(u in complete_prereq[v])
        return result
