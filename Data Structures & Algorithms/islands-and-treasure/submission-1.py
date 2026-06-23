class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    # Add the gate to queue and visited
                    q.append((r, c))
                    visited.add((r, c))

        def addRoom(r, c):
            if min(r, c) < 0 or r == len(grid) or c == len(grid[r]) or (r, c) in visited or grid[r][c] == -1:
                return
            
            visited.add((r, c))
            q.append((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addRoom(r, c+1)
                addRoom(r+1, c)
                addRoom(r, c-1)
                addRoom(r-1, c)

            dist += 1