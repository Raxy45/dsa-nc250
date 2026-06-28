class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ans = float('inf')
        hp = [(0, 0, 0)]
        visited = set()
        R, C = len(heights), len(heights[0])
        while hp:
            # print(hp)
            curr_diff, curr_r, curr_c = heapq.heappop(hp)
            if curr_r == R-1 and curr_c == C-1:
                ans = min(ans, curr_diff)
                return ans
            visited.add((curr_r, curr_c))
            # print('curr', curr_diff, curr_r, curr_c)
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ur, uc = curr_r + dr, curr_c + dc
                # print(ur, uc)
                if min(ur, uc) < 0 or ur==R or uc == C or (ur, uc) in visited:
                    continue
                heapq.heappush(hp, (max(curr_diff, abs(heights[ur][uc] - heights[curr_r][curr_c])), ur, uc))
                # print('added ur uc to hp', hp)
        return ans