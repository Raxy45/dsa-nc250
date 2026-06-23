class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1: return [0]

        # Genarating the graph
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        # Building the egde_cnt and the gathering leaf nodes
        edge_cnt, leaves = {}, deque()
        for node in adj:
            if len(adj[node]) == 1:
                leaves.append(node)
            edge_cnt[node] = len(adj[node])
        

        while leaves:
            if n<=2:
                return list(leaves)
            
            # Starting over one level of leaves at a time
            for _ in range(len(leaves)):
                leaf_node = leaves.popleft()
                n -= 1
                for nei in adj[leaf_node]:
                    # This means you have removed the leaf, 
                    # therefore decrease the degree of its adjacent nodes
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)
            