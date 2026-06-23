class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        for pre_req, og_course in prerequisites:
            graph[og_course].append(pre_req)
        print(graph)
    
        visited = set()
        def dfs(idx):
            if len(graph[idx])==0: return []
            if idx in visited:
                return graph[idx]
            
            curr = []
            visited.add(idx)
            for pre_req in graph[idx]:
                curr.append(pre_req)
                nested_prereqs = dfs(pre_req)
                if len(nested_prereqs)>0:
                    curr.extend(nested_prereqs)
            
            graph[idx] = curr
            return graph[idx]
        
        for i in range(len(graph)):
            dfs(i)
        
        ans=[False]*len(queries)
        for idx, (prereq, course) in enumerate(queries):
            if prereq in graph[course]: ans[idx]=True
        return ans

