class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited, ans = set(), 0
        def dfs(r, c):
            if r<0 or r==len(grid) or c<0 or c==len(grid[0]):
                return True
            
            if (r, c) in visited or grid[r][c]=='0':
                return True
            
            visited.add((r, c))
            top = dfs(r-1, c)
            rhs = dfs(r, c+1)
            bottom = dfs(r+1, c)
            lhs = dfs(r, c-1)
            # print(top, rhs, bottom, lhs, 'for', r,c)

            return top and rhs and bottom and lhs

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and (i, j) not in visited and dfs(i, j):
                    ans += 1
        return ans
        