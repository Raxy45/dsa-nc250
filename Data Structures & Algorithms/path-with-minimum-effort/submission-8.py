class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m = [[float('inf') for _ in range(C)] for _ in range(R)]
        hp = [[0, 0, 0]]
        m[0][0] = 0
        while hp:
            # print(hp)
            effort, r, c = heapq.heappop(hp)
            if r==R-1 and c==C-1:
                return effort
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < R and 0 <= nc < C:
                    edge = abs(heights[nr][nc] - heights[r][c])
                    new_effort = max(effort, edge)

                    if new_effort < m[nr][nc]:
                        m[nr][nc] = new_effort
                        heapq.heappush(hp, (new_effort, nr, nc))
        return -1