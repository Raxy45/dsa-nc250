class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited, ans = set(), 0
        def dfs(r, c):
            # nonlocal curr_area
            if r<0 or r==len(grid) or c<0 or c==len(grid[0]):
                return 0
            
            if (r, c) in visited or grid[r][c]==0:
                return 0
            
            visited.add((r, c))

            return 1 + dfs(r-1, c) + dfs(r, c+1) + dfs(r+1, c) + dfs(r, c-1)
            # return 1 + curr_area
            # print(top, rhs, bottom, lhs, 'for', r,c)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # curr_area = 0
                if grid[i][j] == 1 and (i, j) not in visited:
                    temp = dfs(i, j)
                    # print('area for', i,j, 'is', temp)
                    ans = max(temp, ans)
                    
        return ans
        