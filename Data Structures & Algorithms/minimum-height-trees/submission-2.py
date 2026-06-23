class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1: return [0]

        # TC = O(n) =. O(V+E)
        # SC = O(n)
        # Genarating the graph
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        print(adj)

        edge_count = defaultdict(int)
        leaves = deque()
        visited = set()
        for node, child in adj.items():
            if len(child) == 1:
                visited.add(node)
                leaves.append(node)
            else:
                edge_count[node] = len(child)
        print(edge_count)
        print(leaves)

        while leaves and len(edge_count)>2:
            leaf = leaves.popleft()
            print('leaf',leaf)
            print('leaves', leaves)
            print('edge_count prev', edge_count)
            for parent in adj[leaf]:
                edge_count[parent] -= 1
                if edge_count[parent] == 1 and parent not in visited:
                    visited.add(parent)
                    leaves.append(parent)
                elif edge_count[parent] == 0:
                    del edge_count[parent]
            print('post edge_count', edge_count)
        print(edge_count)
        return list(edge_count.keys())
            