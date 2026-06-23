class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        components = 0
        for u, v in edges:
            if u not in visited and v not in visited:
                components += 1
            visited.add(u)
            visited.add(v)
        return components