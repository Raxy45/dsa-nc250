class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m = [[float('inf') for _ in range(C)] for _ in range(R)]
        hp = [[0, 0, 0]]
        m[0][0] = 0
        while hp:
            print(hp)
            dist, r, c = heapq.heappop(hp)
            if r==R-1 and c==C-1:
                return dist
            
            for dr, dc in directions:
                ur, uc = r+dr, c+dc
                if 0<=ur<R and 0<=uc<C:
                    delta_d = abs(heights[ur][uc] - heights[r][c])
                    dist = max(dist, delta_d)
                    if m[ur][uc] > dist:
                        m[ur][uc] = dist
                        heapq.heappush(hp, [dist, ur, uc])
        return -1