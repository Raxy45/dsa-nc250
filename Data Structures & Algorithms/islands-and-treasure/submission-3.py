from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        R, C = len(grid), len(grid[0])

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r, c, 0))

        while q:
            r, c, steps = q.popleft()

            if r < 0 or r == R or c < 0 or c == C or grid[r][c] == -1 or grid[r][c] < steps:
                continue

            grid[r][c] = steps

            q.append((r, c+1, steps+1))
            q.append((r+1, c, steps+1))
            q.append((r, c-1, steps+1))
            q.append((r-1, c, steps+1))