class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        def dfs(r, c):
            if (r,c) in visited: 
                print(r,c,'is already visited')
                return 0
            if r<0 or r==R or c<0 or c==C:
                print('r went out of bound, adding 1 to curr')
                return 1
            
            if grid[r][c] == 0: 
                print('water for',r,c, 'returning 1')
                return 1
            
            peri = 0
            visited.add((r, c))
            peri += dfs(r, c+1)
            peri += dfs(r+1, c)
            peri += dfs(r, c-1)
            peri += dfs(r-1, c)
            return peri
        visited = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1 and (r,c) not in visited:
                    return dfs(r,c)
                    
