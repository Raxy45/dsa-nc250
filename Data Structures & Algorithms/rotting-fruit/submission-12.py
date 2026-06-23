class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mins = 0
        q = deque([])
        R, C = len(grid), len(grid[0])
        visited = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c]==2:
                    visited.add((r, c))
                    q.append([r, c])
        


        def addFruit(r, c):
            if min(r,c)<0 or r==R or c==C or grid[r][c]==0 or (r,c) in visited:
                return
            
            grid[r][c]=2
            q.append((r, c))
            visited.add((r, c))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                addFruit(r, c+1)
                addFruit(r+1, c)
                addFruit(r, c-1)
                addFruit(r-1, c)
            
            if q:
                mins += 1
            
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    return -1
        return mins

            
