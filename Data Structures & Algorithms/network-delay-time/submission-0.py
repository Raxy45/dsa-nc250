class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        print(graph)

        m = [float('inf')] * (n+1)
        m[k] = 0
        hp = [(0, k)]
        while hp:
            time, node = heapq.heappop(hp)
            print(time, node)
            for neighbour, delta_time in graph[node]:
                updated_time = time + delta_time
                if m[neighbour] > updated_time:
                    m[neighbour] = updated_time
                    heapq.heappush(hp, (updated_time, neighbour))
            print(hp)
            print(m)
            print('88888')
        
        print(m)
        max_time = float('-inf')
        for t in m[1:]:
            if t==float('inf'): return -1
            max_time = max(max_time, t)
        return max_time