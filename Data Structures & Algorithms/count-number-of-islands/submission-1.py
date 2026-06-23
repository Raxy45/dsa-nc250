class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def solve(r, c):
            # print('in for', r, c)
            if r < 0 or r==len(grid) or c<0 or c==len(grid[r]) or (r,c) in seen:
                return 0

            if grid[r][c] == "0": return 0

            current = int(grid[r][c])
            seen.add((r,c))

            current += solve(r, c+1)
            current += solve(r+1, c)
            current += solve(r, c-1)
            current += solve(r-1, c)
            return current

        seen = set()
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                # print('current grid', grid[r][c])
                # print(r, c)
                if grid[r][c] == "1":
                    if solve(r, c):
                        # print('current r, c', r, c)
                        # print('final seen', seen)
                        ans += 1

        return ans
        