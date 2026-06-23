class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        for pre_req, og_course in prerequisites:
            graph[og_course].append(pre_req)
        
        complete_prereq = defaultdict(set)
    
        visited = set()
        def dfs(idx):
            if len(graph[idx])==0: return []
            if idx in complete_prereq:
                return complete_prereq[idx]
            
            curr = []

            visited.add(idx)
            for pre_req in graph[idx]:
                complete_prereq[idx].add(pre_req)
                nested_prereqs = dfs(pre_req)
                complete_prereq[idx].update(nested_prereqs)
            
            return list(complete_prereq[idx])
        
        for i in range(len(graph)):
            dfs(i)
        
        ans=[False]*len(queries)
        for idx, (prereq, course) in enumerate(queries):
            if prereq in complete_prereq[course]: ans[idx]=True
        return ans

