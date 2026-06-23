class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)
    
    def isConnected(self):
        return self.n==1

    def find(self, node):
        if node == self.parent[node]:
            return node
        
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        p_u, p_v = self.find(u), self.find(v)
        if p_u == p_v:
            return False
        
        self.n -= 1
        r_u, r_v = self.rank[p_u], self.rank[p_v]
        if r_v > r_u:
            self.parent[p_u] = self.parent[p_v]
        elif r_u > r_v:
            self.parent[p_v] = self.parent[p_u]
        else:
            self.parent[p_u] = self.parent[p_v]
            self.rank[p_v] += 1
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def Kruskal(indx, include):
            uf = UnionFind(n)
            curr_total_wt = 0

            if include:
                u, v, w, _ = edges[indx]
                if uf.union(u, v):
                    curr_total_wt += w

            for j, (u, v, w, i) in enumerate(edges):
                if j == indx:   # ✅ FIX HERE
                    continue
                
                if uf.union(u, v):
                    curr_total_wt += w

            return curr_total_wt if uf.isConnected() else float('inf')
        
        for i, e in enumerate(edges):
            e.append(i)
        
        edges.sort(key = lambda e : e[2])
        mst_wt = Kruskal(-1, False)
        critical, pseudo = [], []
        for idx, (u, v, w, i) in enumerate(edges):
            print(u, v, w, i, 'herr')
            if Kruskal(idx, False) > mst_wt:
                # if you skipped the node, wt increases -> cant be skipped
                critical.append(i)
            elif Kruskal(idx, True)==mst_wt:
                # if you begin with the ith index edge and mst_wt remains same
                # this means even if you skipped the edge(above condition) -> mst remains same unaffected without this edge
                # and even if you included the edge mst remains same i.e. you can genarate mst with this edge
                # this is optional edge
                pseudo.append(i)
        return [critical, pseudo]