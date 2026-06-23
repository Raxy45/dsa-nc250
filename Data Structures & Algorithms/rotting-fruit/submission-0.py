class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mins = 0
        visited, q = set(), deque()
        for r in range(len(grid)):
            for c in range((len(grid[r]))):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
        
        def FruitRot(r, c):
            if min(r, c) < 0 or r == len(grid) or c == len(grid[r]) or (r, c) in visited or grid[r][c] == 0 or grid[r][c]==2:
                return
            
            q.append((r, c))
            visited.add((r, c))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                FruitRot(r, c+1)
                FruitRot(r+1, c)
                FruitRot(r, c-1)
                FruitRot(r-1, c)
            if q:
                mins += 1
        
        return mins if mins!=0 else -1