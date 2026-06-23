class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mins = 0
        q = deque()
        for r in range(len(grid)):
            for c in range((len(grid[r]))):
                if grid[r][c] == 2:
                    q.append((r, c))
        
        def FruitRot(r, c):
            if min(r, c) < 0 or r == len(grid) or c == len(grid[r]) or grid[r][c] == 0 or grid[r][c]==2:
                return
            
            q.append((r, c))
            grid[r][c] = 2

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                FruitRot(r, c+1)
                FruitRot(r+1, c)
                FruitRot(r, c-1)
                FruitRot(r-1, c)
            if q:
                mins += 1
        
        # Before returning mins, we have to check if there exists some fresh fruit
        # which did not got rot
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    return -1

        # if minutes passed by and no fresh fruit present, return the minutes
        return mins