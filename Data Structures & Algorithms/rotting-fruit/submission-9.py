class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        v = set()
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c]==2:
                    q.append((r, c))
        
        def addFruit(r, c):
            if min(r, c)<0 or r==R or c==C or grid[r][c]==0 or (r, c) in v:
                return
            
            q.append((r, c))
            grid[r][c] = 2
            v.add((r, c))
        mins = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                addFruit(r, c+1)
                addFruit(r+1, c)
                addFruit(r, c-1)
                addFruit(r-1, c)
            if q:
                mins += 1
        
        print(grid)
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    return -1
        return mins if mins>0 else -1