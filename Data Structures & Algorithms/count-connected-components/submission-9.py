class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        components = 0
        for u, v in edges:
            if u not in visited and v not in visited:
                components += 1
            visited.add(u)
            visited.add(v)
        for i in range(n):
            if i not in visited:
                components += 1
        return components