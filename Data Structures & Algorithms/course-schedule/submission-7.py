class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for a, b in prerequisites:
            if a not in graph:
                graph[a] = []
            graph[a].append(b)
        
        visited = set()
        def dfs(curr):
            nonlocal visited
            if curr not in graph:
                # given course does not have dependency
                return True
            
            # current course has dependency
            visited.add(curr)
            for curr_course_prereq in graph[curr]:
                if curr_course_prereq in visited:
                    return False
                if not dfs(curr_course_prereq):
                    return False
                
            visited.remove(curr)
            graph[curr] = []
            return True
        
        for i in range(numCourses):
            if i in graph and not dfs(i):
                return False
        return True
