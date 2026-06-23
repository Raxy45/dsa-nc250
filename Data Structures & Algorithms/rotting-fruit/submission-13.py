class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        R, C = len(grid), len(grid[0])
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    q.append((i, j))
        
        time = -1
        c = 0
        print(q)
        # return 1
        while q:
            print('current time', time, 'queue', q)
            for _ in range(len(q)):
                # if c>1:
                #     break
                c += 1
                r, c = q.popleft()
                if r<0 or r==R or c<0 or c==C or grid[r][c] == 0 or grid[r][c]==-1:
                    continue
                
                print('current', r, c)
                grid[r][c] = -1
                q.append((r, c+1))
                q.append((r+1, c))
                q.append((r, c-1))
                q.append((r-1, c))
            if q:
                time += 1
        

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1: return -1
        return time

        