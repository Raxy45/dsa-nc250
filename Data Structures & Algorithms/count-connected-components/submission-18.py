class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        for u, v in edges:
            if (u not in visited or v not in visited):
                visited.add(u)
                visited.add(v)
                n -=1
        return n
