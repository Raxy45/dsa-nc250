class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        q = deque([points[0]])
        visited = set()
        ans = 0

        while q:
            min_d, temp_q = float('inf'), deque([])
            curr_x, curr_y = q.popleft()
            for x, y in points:
                if (x, y) not in visited:
                    if (abs(curr_x - x) + abs(curr_y - y)) <= min_d:
                        min_d = abs(curr_x - x) + abs(curr_y - y)
                        temp_q.append((x, y))
            
            while temp_q:
                curr_pair = temp_q.popleft()
                visited.add(curr_pair)
                q.append(curr_pair)
                ans += abs(curr_pair[0] - curr_x) + abs(curr_pair[1] - curr_y)
                print('For', curr_x, curr_y, 'min pair is', curr_pair, 'ans is', ans)
        return ans