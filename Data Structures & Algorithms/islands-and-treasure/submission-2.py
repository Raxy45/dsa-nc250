class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C, visited = len(grid), len(grid[0]), set()
        def solve(r, c, steps):
            if r<0 or r==R or c<0 or c==C or grid[r][c] == -1:
                return
            
            if (r, c) in visited and steps>grid[r][c]:
                return

            if grid[r][c]==0 and (r, c) not in visited:
                return
            visited.add((r, c))
            print('setting',r,c, 'to steps', steps)
            grid[r][c] = steps
            solve(r, c+1, steps+1)
            solve(r+1, c, steps+1)
            solve(r, c-1, steps+1)
            solve(r-1, c, steps+1)
        for r in range(R):
            for c in range(C):
                if grid[r][c]==0:
                    visited.add((r, c))
                    print('going in')
                    solve(r, c, 0)
        # return grid
