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
        # TC:
        # build graph -> o(e) e is number of edges
        # iterating for heap:
        # max elems stored in heap, each node having n-1 neighbours = n *n-1 = n^2?
        # heap pop is 2 log N
        # E + N^2 * 2 LogN 

        # Sc is N^2, N(for time_list)
        time_list[k] = 0
        hp = [(0, k)]
        while hp:
            curr_time, curr_src = heapq.heappop(hp)
            if curr_src not in graph or curr_time > time_list[curr_src]: continue
            for nei, nei_time in graph[curr_src]:
                if (curr_time + nei_time) < time_list[nei]:
                    time_list[nei] =  (curr_time + nei_time)
                    heapq.heappush(hp, (curr_time + nei_time, nei))
        return max(time_list[1:]) if max(time_list[1:]) != float('inf') else -1