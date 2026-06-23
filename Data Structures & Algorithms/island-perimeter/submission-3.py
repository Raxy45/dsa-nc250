class Solution:
    def islandPerimeter(self, grid):
        def solve(r, c):
            if r<0 or r==len(grid) or c<0 or c==len(grid):
                return 1
            
            if grid[r][c] == 0:
                return 1

            if (r,c) in visited:
                return 0

            peri = 0
            visited.add((r, c))
            peri += solve(r, c+1)
            peri += solve(r+1, c)
            peri += solve(r, c-1)
            peri += solve(r-1, c)

            return peri
        
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    return solve(r, c)

    def islandPerimeterME(self, grid: List[List[int]]) -> int:
        def solve(r, c, seen):
            nonlocal peri
            if r<0 or r==len(grid) or c<0 or c==len(grid[r]) or grid[r][c] == 0:
                return 0

            if (r,c) in seen:
                return 1
            current = 4
            seen.add((r, c))
            rhs_peri = solve(r, c+1, seen)
            bottom_peri = solve(r+1, c, seen)
            lhs_peri = solve(r, c-1, seen)
            top_peri = solve(r-1, c, seen)

            if rhs_peri>0:
                current -= 1
            
            if bottom_peri > 0:
                current -= 1

            if lhs_peri > 0:
                current -= 1
            
            if top_peri > 0:
                current -= 1
            
            # seen.remove((r,c))
            peri += current

            return peri
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0: 
                    continue
                peri = 0
                seen = set()
                solve(r,c, seen)
                return peri