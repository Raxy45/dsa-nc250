class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {i: [] for i in range(numCourses)}
        for pre, course in prerequisites:
            graph[course].append(pre)
        
        prereq_set = defaultdict(set)

        def dfs(course):
            if course in prereq_set:
                return prereq_set[course]

            if course not in graph:
                return []
            
            current_prereq_list = graph[course]
            for curr_pre in current_prereq_list:
                current_prereq_list.extend(dfs(curr_pre))
            prereq_set[course] = current_prereq_list
            return set(prereq_set[course])
        
        for i in range(numCourses):
            dfs(i)
        
        ans = []
        for u, v in queries:
            if u in prereq_set[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
