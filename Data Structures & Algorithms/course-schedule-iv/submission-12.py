class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {i: [] for i in range(numCourses)}
        for pre, course in prerequisites:
            graph[course].append(pre)
        
        prereq_set = defaultdict(set)

        def dfs(course):
            if course in prereq_set:
                # we have traversed all the deps of this
                return prereq_set[course]

            if course not in graph:
                return []
            
            current_prereq_list = set(graph[course])
            for curr_pre in graph[course]:
                current_prereq_list.update(dfs(curr_pre))
            prereq_set[course] = current_prereq_list
            return prereq_set[course]
        
        for i in range(numCourses):
            dfs(i)
        
        ans = []
        for u, v in queries:
            if u in prereq_set[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
