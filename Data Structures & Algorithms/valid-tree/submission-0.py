class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        visit, cycle = set(), set()

        for src, dest in edges:
            graph[src].append(dest)

        
        def solve(start):
            print(start, visit)
            if start in visit:
                return False

            for child in graph[start]:
                if not solve(child): return False

            visit.add(start)
            return True

        print(graph)
        for i in range(n):
            if i not in visit:
                if not solve(i): return False
        return True
