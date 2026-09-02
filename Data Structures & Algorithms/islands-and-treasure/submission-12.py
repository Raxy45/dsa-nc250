class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque([])
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==0:
                    q.append((i, j))

        t = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # print(q)÷
        while q:
            # print('b4 t', t, q)
            # print(visited)
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                grid[r][c] = t
                for dr, dc in dirs:
                    ur, uc = r + dr, c + dc
                    if min(ur, uc) < 0 or ur==len(grid) or uc==len(grid[0]) or grid[ur][uc]==-1 or (ur, uc) in visited:
                        continue
                    q.append((ur, uc))
            t += 1
