class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        q = deque([])
        for node, nei in graph.items():
            if len(nei) == 1:
                q.append(node)
        print('leaf nodes', q)
        while q:
            if len(graph) <=2:
                break
            for _ in range(len(q)):
                node = q.popleft()
                print('current leaf', node)
                for nei in graph[node]:
                    print('removing from', nei)
                    graph[nei].remove(node)
                    if len(graph[nei]) == 1:
                        print('nei became a leaf node', nei)
                        q.append(nei) 
                
                del graph[node]
        print(graph)
        return list(graph.keys())