class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mins = 0
        q = deque()
        for r in range(len(grid)):
            for c in range((len(grid[r]))):
                if grid[r][c] == 2:
                    q.append((r, c))
        
        def FruitRot(r, c):
            if min(r, c) < 0 or r == len(grid) or c == len(grid[r]) or grid[r][c] == 0 or grid[r][c]==2:
                return
            
            q.append((r, c))
            grid[r][c] = 2

        print(q)
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for nr, nc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    updated_r, updated_c =  r + nr, c + nc
                    # print(r in range(len(grid)))
                    # print(c in range(len(grid[0])))
                    if (updated_r in range(len(grid))
                            and updated_c in range(len(grid[0]))
                            and grid[updated_r][updated_c] == 1
                        ):
                            print(grid[updated_r][updated_c])
                            grid[updated_r][updated_c] = 2
                            q.append((updated_r, updated_c))
                print(q)
            if q:
                mins += 1
        
        # Before returning mins, we have to check if there exists some fresh fruit
        # which did not got rot
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    return -1

        # if minutes passed by and no fresh fruit present, return the minutes
        return mins