class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time_list = [float('inf')] * (n+1)
        time_list

        graph = {}
        for s,d,t in times:
            if s not in graph:
                graph[s] = []
            graph[s].append((d, t))
        # print(graph, time_list)
        
        time_list[k] = 0
        hp = [(0, k)]
        while hp:
            curr_time, curr_src = heapq.heappop(hp)
            if curr_src not in graph: continue
            for nei, nei_time in graph[curr_src]:
                if (curr_time + nei_time) < time_list[nei]:
                    time_list[nei] =  (curr_time + nei_time)
                    heapq.heappush(hp, (curr_time + nei_time, nei))
        return max(time_list[1:]) if max(time_list[1:]) != float('inf') else -1