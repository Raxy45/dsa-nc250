class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        test_matrix = [[float('inf') for _ in range(C)] for _ in range(R)]
        hp = [[0,0,0]]
        while hp:
            diff, r, c = heapq.heappop(hp)
            if r==R-1 and c==C-1: return diff

            for d_r, d_c in directions:
                u_r, u_c = r + d_r, c + d_c
                if min(u_r, u_c)< 0 or u_r == R or u_c == C:
                    continue
                
                updated_diff = max(diff, abs(heights[r][c] - heights[u_r][u_c]))
                if updated_diff < test_matrix[u_r][u_c]:
                    test_matrix[u_r][u_c] = updated_diff
                    heapq.heappush(hp, (updated_diff, u_r, u_c))