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

        while leaves:
            if n<=2: return list(leaves)

            for _ in range(len(leaves)):
                n -= 1
                leaf = leaves.popleft()
                for parent in adj[leaf]:
                    edge_count[parent] -= 1
                    if edge_count[parent] == 1:
                        leaves.append(parent)
            print('post edge_count', edge_count)
            