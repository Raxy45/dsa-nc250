class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append((i, j, 0))

        counter = 0
        visited = set()
        while q:
            r, c, steps = q.popleft()
            if r<0 or r==len(grid) or c<0 or c==len(grid[0]) \
            or grid[r][c] == -1 or (r, c) in visited:
                continue
            
            
            visited.add((r, c))
            grid[r][c] = steps
            q.append((r, c+1, steps+1))
            q.append((r, c-1, steps+1))
            q.append((r+1, c, steps+1))
            q.append((r-1, c, steps+1))

        
