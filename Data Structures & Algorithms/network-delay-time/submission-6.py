class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        m = [float('inf') for _ in range(n+1)]
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append([v, t])
        
        print(
            graph
        )
        hp = [[0, k]]
        m[k] = 0
        visited = set()
        while hp:
            print(hp)
            print(m)
            curr_time, node = heapq.heappop(hp)
            if node in visited: 
                continue
            
            for nei, time in graph[node]:
                if m[nei] > (time + curr_time):
                    m[nei] = time + curr_time
                    heapq.heappush(hp, (time+curr_time, nei))
            visited.add(node)
        
        ans = -1
        for i in m[1:]:
            if i == float('inf'):
                return -1
            ans = max(ans, i)
        return ans