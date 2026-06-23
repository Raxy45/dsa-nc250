class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def solve(r, c):
            if r<0 or r==len(grid) or c<0 or c==len(grid[r]) or (r,c) in seen:
                return 0

            if grid[r][c] == 0: return 0
            seen.add((r,c))
            current_area = int(grid[r][c])
            current_area += solve(r, c+1)
            current_area += solve(r+1, c)
            current_area += solve(r, c-1)
            current_area += solve(r-1, c)
            return current_area

        max_a = 0
        seen = set()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1 and (r,c) not in seen:
                    max_a = max(solve(r,c), max_a)
        return max_a