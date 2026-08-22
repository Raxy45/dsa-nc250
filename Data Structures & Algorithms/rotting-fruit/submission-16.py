class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i, j))
        
        t = 0
        dirs = [(0, 1), (1, 0), (0, -1),  (-1, 0)]
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for dr, dc in dirs:
                    ur, uc = i + dr, j + dc
                    if min(ur, uc)<0 or max(ur, uc) == len(grid) or grid[ur][uc] != 1:
                        continue
                    grid[ur][uc] = 2
                    q.append((ur, uc))
            if q: t += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        return t
        